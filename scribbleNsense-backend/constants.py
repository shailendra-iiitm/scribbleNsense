# constants.py
from dotenv import load_dotenv
import os

load_dotenv()

SERVER_URL = 'localhost'
PORT = int(os.getenv('PORT', 8900))  # Use environment variable or fallback to 8900
ENV = os.getenv('ENV', 'dev')  # Use environment variable or fallback to 'dev'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Math symbol constants for LaTeX rendering
MATH_SYMBOLS = {
    'pi': r'\pi',
    'theta': r'\theta',
    'alpha': r'\alpha',
    'beta': r'\beta',
    'gamma': r'\gamma',
    'delta': r'\delta',
    'epsilon': r'\epsilon',
    'lambda': r'\lambda',
    'mu': r'\mu',
    'sigma': r'\sigma',
    'phi': r'\phi',
    'omega': r'\omega',
    'infinity': r'\infty',
    'integral': r'\int',
    'sum': r'\sum',
    'sqrt': r'\sqrt',
    'frac': r'\frac',
    'partial': r'\partial',
    'nabla': r'\nabla'
}
