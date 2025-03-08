import math

import numpy as np

from baccarat import Simulator, UniformParam, StaticParam, GaussianParam


class GammaRaySim(Simulator):
    initial_energy_mev = StaticParam(0.663)
    scatter_probability = UniformParam(0, 1)
    scattering_angle = UniformParam(0, 2*math.pi)
    scattering_angle_outcome = UniformParam(0, 1)
    energy_smear_factor = GaussianParam(0, 1)

    def __init__(self, num_samples: int):
        super().__init__(num_samples)
        self.energy_mev = np.empty(num_samples)

    def simulation(self):
        # Get initial parameters as numpy arrays
        initial_energy = self.initial_energy_mev
        scatter_prob = self.scatter_probability
        scatter_angles = self.scattering_angle
        scatter_outcome = self.scattering_angle_outcome
        
        # Update energy_mev to match the shape of initial_energy
        self.energy_mev = initial_energy.copy()
        
        # Get scattering angles and energies
        theta = self.get_scattering_angles(scatter_outcome, scatter_angles)
        scatter_energies = self.compton_scatter_energy(theta)
        
        # Calculate final energy
        energy_mev = np.where(
            scatter_prob < self.get_scatter_probability(), 
            initial_energy - scatter_energies, 
            initial_energy
        )

        return energy_mev

    #####################
    # PHYSICS FUNCTIONS #
    #####################
    @property
    def alpha(self):
        return self.energy_mev / 0.511

    def probability_compton_scatter(self) -> np.ndarray:
        """Probability of Compton scattering."""
        return 1.04713 * np.exp(0.23 * np.exp(-0.5 * self.energy_mev))

    def probability_photoelectic_absorption(self) -> np.ndarray:
        """Probability of photoelectric absorption."""
        return 1.01158 * 10**(132 * np.exp(-28 * self.energy_mev))

    def get_scatter_probability(self) -> np.ndarray:
        """Probability of scattering."""
        p_scatter = self.probability_compton_scatter()
        p_absorb = self.probability_photoelectic_absorption()
        return p_scatter / (p_scatter + p_absorb)
        
    def get_scattering_angles(self, initial_scatter_outcomes: np.ndarray, initial_scatter_angles: np.ndarray) -> np.ndarray:
        """Returns the scattering angles."""
        angles = initial_scatter_angles.copy()
        outcomes = initial_scatter_outcomes.copy()
        
        # Get the Klein-Nishina probability for all angles
        klein_nishina_probs = self.probability_klein_nishina(angles)
        
        # Find indices where outcome is greater than or equal to Klein-Nishina probability
        invalid_mask = outcomes >= klein_nishina_probs
        
        if not np.any(invalid_mask):
            return angles
        
        # Process invalid indices in a vectorized way
        max_iterations = 50  # Prevent infinite loops
        
        for _ in range(max_iterations):
            if not np.any(invalid_mask):
                break
                
            # Generate new angles and outcomes only for invalid points
            new_angles = self.rng.uniform(0, 2*math.pi, size=np.sum(invalid_mask))
            new_outcomes = self.rng.uniform(0, 1, size=np.sum(invalid_mask))
            
            # Update the invalid elements
            angles[invalid_mask] = new_angles
            outcomes[invalid_mask] = new_outcomes
            
            # Recalculate Klein-Nishina probabilities
            klein_nishina_probs = self.probability_klein_nishina(angles)
            
            # Update the invalid mask
            invalid_mask = outcomes >= klein_nishina_probs
        
        return angles

    def compton_scatter_energy(self, theta: np.ndarray) -> np.ndarray:
        """
        Sets the energy to the new energy of the scattered photon.

        Parameters:
            theta (float): The scattering angle in radians.

        Returns:
            float: The new energy of the scattered photon.
        """
        return self.energy_mev / (1 + (self.alpha) * (1 - np.cos(theta)))
        
    def probability_klein_nishina(self, theta: np.ndarray) -> np.ndarray:
        """Probability that the photon is scattered at some angle."""
        cos_theta = np.cos(theta)
        a = 1 / (1 + self.alpha * (1 - cos_theta))
        b = (1 + cos_theta**2) / 2
        c = self.alpha**2 * (1 - cos_theta**2)
        d = (1 + cos_theta**2) * ((1 + self.alpha * (1 - cos_theta)))
        return a**2 * b * (1 + c / d)

    # This function is used in the "large detector regime" (not simulated here)
    def smear(self) -> np.ndarray:
        return self.energy_mev + 0.01 * self.energy_mev * self.energy_smear_factor


if __name__ == "__main__":
    sim = GammaRaySim(1_000_000)
    res = sim.run()
    # Try adding a histogram of the results yourself!
    print("First ten results:")
    print(res[:10])
