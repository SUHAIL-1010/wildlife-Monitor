import kagglehub

class DatasetIntegrator:

    @staticmethod
    def verify_serengeti():
        """1. Snapshot Serengeti Dataset (Camera Trap Images)"""
        # Source: https://www.kaggle.com/datasets/silviamatoke/serengeti-dataset
        path = kagglehub.dataset_download("silviamatoke/serengeti-dataset")
        return {"dataset": "Serengeti Dataset", "status": "Connected", "path": path}

    @staticmethod
    def verify_inaturalist():
        """2. iNaturalist Dataset (Biodiversity & Species Recognition)"""
        # Source: https://ml-inat-competition-datasets.s3.amazonaws.com/2021/val.tar.gz
        return {
            "dataset": "iNaturalist 2021", 
            "status": "Ready for Wget/cURL stream", 
            "url": "https://ml-inat-competition-datasets.s3.amazonaws.com/2021/val.tar.gz"
        }

    @staticmethod
    def verify_birdclef():
        """3. BirdCLEF 2026 Dataset (Bioacoustic Analysis)"""
        # Source: https://www.kaggle.com/competitions/birdclef-2026/data
        path = kagglehub.competition_download("birdclef-2026")
        return {"dataset": "BirdCLEF 2026", "status": "Connected", "path": path}

    @staticmethod
    def verify_animal_kingdom():
        """4. Animal Kingdom 90 Dataset (Species Identification)"""
        # Source: https://www.kaggle.com/datasets/sanadalali/animal-categories-90-masters-of-survival
        path = kagglehub.dataset_download("sanadalali/animal-categories-90-masters-of-survival")
        return {"dataset": "Animal Kingdom 90", "status": "Connected", "path": path}

    @staticmethod
    def verify_gbif():
        """5. GBIF Species Occurrences (Spatial & Population Data)"""
        # Source: https://www.kaggle.com/datasets/anjalibarge2511/gbif-species-occurrence-records
        path = kagglehub.dataset_download("anjalibarge2511/gbif-species-occurrence-records")
        return {"dataset": "GBIF Occurrences", "status": "Connected", "path": path}