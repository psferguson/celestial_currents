
from celestialcurrents.utils.load_data import MapLoader
import numpy as np

class SurveyConfig:
    # make init function
    def get_map_loader(self, z, age, mag_max, mag_min):
        self.map_loader = MapLoader(survey=self.survey,
                                    data_directory=self.data_directory,
                                    z=z,
                                    age=age,
                                    mag_max=mag_max,
                                    mag_min=mag_min,
                                    name_fstring=None)
        
        self.load_data = self.map_loader.load_data
        

class DECaLS_DR10( SurveyConfig):
    def __init__(self):
        # hpxcube creation
        self.survey = 'DECaLS_DR10'
        self.mag = 'MAG_SFD_%s'
        self.ext = None
        self.data_directory = '/home/fergie/software/celestial_currents/data/DECaLS_DR10/'
        self.name_fstring = "{survey}_iso_hpxcube_z{z:.4f}_a{age:.1f}_gmax{mag_max}_gmin{mag_min}.fits.gz"
        self.fracdet = None
        self.mag_min = 16
        self.mag_max = 23.5
        self.stargal = None
        self.stargal_cut = None
        self.err = lambda x: 0.0010908679647672335 + np.exp((x - 27.091072029215375) / 1.0904624484538419)
        self.C = [0.05, 0.1]
        self.E = 2.
        self.moduli = [15., 20.]

class DES_Y6(SurveyConfig):
    def __init__(self):
        # hpxcube creation
        self.survey = 'DES_Y6_GOLD'
        self.mag = 'SOF_PSF_MAG_CORRECTED_%s'
        self.ext = None
        self.data_directory = '/home/fergie/software/celestial_currents/data/DES_Y6_GOLD/'
        self.name_fstring = "{survey}_iso_hpxcube_z{z:.4f}_a{age:.1f}_gmax{mag_max}_gmin{mag_min}.fits.gz"
        self.fracdet = None
        self.mag_min = 16.
        self.mag_max = 24.0
        self.stargal = 'EXT_SOF'
        self.stargal_cut = 1
        self.err = lambda x: 0.0010908679647672335 + np.exp((x - 27.091072029215375) / 1.0904624484538419)
        self.C = [0.05, 0.1]
        self.E = 2.
        self.moduli = [15., 20.]