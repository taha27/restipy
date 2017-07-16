"""
Entry point for this custom API server
"""
from api import app

if __name__ == '__main__':
    app.run(debug=True)
