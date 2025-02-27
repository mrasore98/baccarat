import math

from baccarat import Simulator, UniformParam, StaticParam, GaussianParam


class GammaRaySim(Simulator):
    initial_energy_mev = StaticParam(0.663)
    scatter_probability = UniformParam(0, 1)
    scattering_angle = UniformParam(0, 2*math.pi)
    scattering_angle_outcome = UniformParam(0, 1)
    energy_smear_factor = GaussianParam(0, 1)

    def __init__(self, num_samples: int, max_workers: int | None = None):
        super().__init__(num_samples, max_workers)
        self.energy_mev = self.initial_energy_mev

    def simulation(self):
        self.energy_mev = self.initial_energy_mev
        scatter_probability = self.scatter_probability

        # Compton scattering condition
        if scatter_probability < self.get_scatter_probability():
            scatter_angle_determined = False
            while not scatter_angle_determined:
                theta = self.scattering_angle
                scatter_angle_determined = self.scattering_angle_outcome < self.probability_klein_nishina(theta)
            self.compton_scatter_energy(theta)
            energy_mev = self.initial_energy_mev - self.energy_mev
        else:
            energy_mev = self.energy_mev

        return energy_mev

    #####################
    # PHYSICS FUNCTIONS #
    #####################
    @property
    def alpha(self):
        return self.energy_mev / 0.511

    def probability_compton_scatter(self):
        """Probability of Compton scattering."""
        return 1.04713 * math.exp(0.23 * math.exp(-0.5 * self.energy_mev))

    def probability_photoelectic_absorption(self) -> float:
        """Probability of photoelectric absorption."""
        return 1.01158 * 10**(132 * math.exp(-28 * self.energy_mev))

    def get_scatter_probability(self) -> float:
        """Probability of scattering."""
        p_scatter = self.probability_compton_scatter()
        p_absorb = self.probability_photoelectic_absorption()
        return p_scatter / (p_scatter + p_absorb)

    def compton_scatter_energy(self, theta: float) -> None:
        """
        Sets the energy to the new energy of the scattered photon.

        Parameters:
            theta (float): The scattering angle in radians.

        Returns:
            float: The new energy of the scattered photon.
        """
        self.energy_mv = self.energy_mev / (1 + self.alpha * (1 - math.cos(theta)))

    def probability_klein_nishina(self, theta: float) -> float:
        """Probability that the photon is scattered at some angle."""
        cos_theta = math.cos(theta)
        a = 1 / (1 + self.alpha * (1 - cos_theta))
        b = (1 + cos_theta**2) / 2
        c = self.alpha**2 * (1 - cos_theta**2)
        d = (1 + cos_theta**2) * ((1 + self.alpha * (1 - cos_theta)))
        return a**2 * b * (1 + c / d)

    # This function is used in the "large detector regime" (not simulated here)
    def smear(self) -> float:
        return self.energy_mev + 0.01 * self.energy_mev * self.energy_smear_factor


if __name__ == "__main__":
    sim = GammaRaySim(10_000)
    res = sim.run()
    # Try adding a histogram of the results yourself!
    print("First ten results:")
    print(res[:10])
