import os, sys
import pytest
from dotenv import load_dotenv

load_dotenv(dotenv_path="../resources/.env")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
