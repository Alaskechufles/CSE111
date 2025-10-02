from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest 
from pytest import approx

def test_water_column_height():
    """Verify that the water_column_height function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the water_column_height function and verify that it returns a float.
    height = water_column_height(10, 5)
    assert isinstance(height, float), "water_column_height function must return a float"

    # Call the water_column_height function ten times and use an assert
    # statement to verify that the float returned by the
    # water_column_height function is correct each time.
    assert water_column_height(0, 0) == 0.0
    assert water_column_height(0, 10) == 7.5
    assert water_column_height(25, 0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    """Verify that the pressure_gain_from_water_height function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the pressure_gain_from_water_height function and verify that it returns a float.
    pressure = pressure_gain_from_water_height(10)
    assert isinstance(pressure, float), "pressure_gain_from_water_height function must return a float"

    # Call the pressure_gain_from_water_height function ten times and use an assert
    # statement to verify that the float returned by the
    # pressure_gain_from_water_height function is correct each time.
    assert pressure_gain_from_water_height(0) == 0.0
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.1)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.1)
   
def test_pressure_loss_from_pipe():
    """Verify that the pressure_loss_from_pipe function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the pressure_loss_from_pipe function and verify that it returns a float.
    loss = pressure_loss_from_pipe(0.1, 10, 0.02, 2)
    assert isinstance(loss, float), "pressure_loss_from_pipe function must return a float"

    # Call the pressure_loss_from_pipe function ten times and use an assert
    # statement to verify that the float returned by the
    # pressure_loss_from_pipe function is correct each time.

    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0, abs=0.01)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0, abs=0.01)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0, abs=0.01)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.01)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.01)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.01)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.01)

def test_pressure_loss_from_fittings():
    """Verify that the pressure_loss_from_fittings function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the pressure_loss_from_fittings function and verify that it returns a float.
    loss = pressure_loss_from_fittings(2, 3)
    assert isinstance(loss, float), "pressure_loss_from_fittings function must return a float"

    # Call the pressure_loss_from_fittings function ten times and use an assert
    # statement to verify that the float returned by the
    # pressure_loss_from_fittings function is correct each time.

    assert pressure_loss_from_fittings(0.00, 3) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    """Verify that the reynolds_number function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the reynolds_number function and verify that it returns a float.
    reynolds = reynolds_number(0.1, 2)
    assert isinstance(reynolds, float), "reynolds_number function must return a float"

    # Call the reynolds_number function ten times and use an assert
    # statement to verify that the float returned by the
    # reynolds_number function is correct each time.

    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    """Verify that the pressure_loss_from_pipe_reduction function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the pressure_loss_from_pipe_reduction function and verify that it returns a float.
    loss = pressure_loss_from_pipe_reduction(0.1, 2, 10000, 0.05)
    assert isinstance(loss, float), "pressure_loss_from_pipe_reduction function must return a float"

    # Call the pressure_loss_from_pipe_reduction function ten times and use an assert
    # statement to verify that the float returned by the
    # pressure_loss_from_pipe_reduction function is correct each time.

    assert pressure_loss_from_pipe_reduction(0.286870, 0.00, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.286870, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.286870, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)
   

pytest.main(["-v", "--tb=line", "-rN", __file__])
