
import os, sys
_filepath = os.path.dirname(sys.argv[0])
if sys.version_info[0] == 3:
    import you_get
    if __name__ == '__main__':
        you_get.main(repo_path=_filepath)
else: # Python 2
    from you_get.util import log
    log.e("[fatal] Python 3 is required!")
    log.wtf("try to run this script using 'python3 you-get'.")
