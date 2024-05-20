# class to load in healpix/healsparse data 
import fitsio
import numpy as np
import os 
from .log import logger




class MapLoader:
    def __init__(self, survey, data_directory, z, age, mag_max,mag_min,name_fstring=None):
        self.survey = survey
        self.data_directory = data_directory
        self.z = z # metallicity 
        self.age = age 
        self.mag_max = mag_max
        self.mag_min = mag_min
        self.name_fstring = name_fstring
    
    def get_filename(self,name_fstring=None):
        if name_fstring is None:
            name_fstring = "{survey}_iso_hpxcube_z{z:.4f}_a{age:.1f}_gmax{mag_max}_gmin{mag_min}.fits.gz"

        filename = self.data_directory + name_fstring.format(survey=self.survey, z=self.z, age=self.age, mag_max=self.mag_max, mag_min=int(self.mag_min)) 
        return filename
    
    def load_data(self):
        filename = self.get_filename(name_fstring=self.name_fstring)
        
        hpxcube, fracdet, modulus = self.load_hpxcube(filename)
        return hpxcube, fracdet, modulus
    
    @staticmethod
    def load_hpxcube(filename):
        if not os.path.exists(filename):
            logger.info(f"{filename} does not exist")
            raise FileNotFoundError

        logger.info(f"Reading {filename}...")
        
        with fitsio.FITS(filename) as f:
            if 'HPXCUBE' not in f:
                logger.error(f"HPXCUBE extension not found in {filename}")
                raise ValueError
            else:
                hpxcube = f['HPXCUBE'].read()
            
            if 'FRACDET' not in f:
                logger.debug(f"skipping fracdet...")
                fracdet = None
            else:
                fracdet = f['FRACDET'].read()
                logger.info(f'fracdet read with {np.sum(fracdet > 0.5)} covered pixels')

            if 'MODULUS' not in f:
                logger.debug('no modulus array found...')
                modulus = np.array([16.])
            else:
                modulus = f['MODULUS'].read()
        return hpxcube, fracdet, modulus
    @staticmethod
    def load_hspcube(filename):
        raise NotImplementedError