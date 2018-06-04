# Setup TAB key for auto-complete
import atexit, rlcompleter, readline
readline.parse_and_bind('tab: complete')

# Add $HOME to sys.path
import sys, os
homePath = os.path.expanduser('~')
if homePath not in sys.path:
    sys.path.append(homePath)

#
