"""
Launch the doris app
"""
import os
from doris.app import app

if __name__ == "__main__":
    port = str(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
