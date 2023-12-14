from dynaconf import Dynaconf

settings = Dynaconf(load_dotenv=True, dotenv_path="../envs/.env")
