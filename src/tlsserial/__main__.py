import sys
from .cli import main

rc = 1
try:
    main()
    rc = 0
except Exception as e:
    print("Error:", e, file=sys.stderr)
sys.exit(rc)
