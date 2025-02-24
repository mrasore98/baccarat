import pytest

from baccarat import Simulator, UniformParam, StaticParam

def test_approximate_pi():
    class PiSimulator(Simulator):
        def simulation(self):
            # Use assignments since attribute access will generate the random value
            x, y, r = self.x, self.y, self.r
            # Check to see if the random point is inside the circle
            return x**2 + y**2 <= r**2
        
        def compile_results(self):
            return 4 * len([res for res in self.results if res]) / len(self.results)
    
    params = [
        UniformParam('x', -1, 1),
        UniformParam('y', -1, 1),
        StaticParam('r', 1),
    ]
    approx_pi = PiSimulator(1_000_000, params).run()
    assert pytest.approx(3.14159, rel=0.01) == approx_pi