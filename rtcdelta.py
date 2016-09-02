"""RTC Delta

Usage:
  rtcdelta      --user=<username> --pass=<password> --url=<rtcUrl> --workitem=<id>  --beforePath=<beforePath> --afterPath=<afterPath> \r\n \
                [--endsWithJazz] [--logs]

Options:
  --user=<username>         Username, for RTC authentication.
  --pass=<password>         Password, for RTC authentication.
  --url=<rtcUrl>            RTC URL.
  --workitem=<id>           ID of the work item we want to analyze.
  --beforePath=<beforePath> Path into where perform the checkout of the file before the changes
  --afterPath=<afterPath>   Path into where perform the checkout of the file after the changes
  --endsWithJazz            If your url ends with ccm, no neet to set to True.
  --logs                    If you want to see log lines in the console


Author:
  Marcio Marchini (marcio@BetterDeveloper.net)

"""

from docopt import docopt
from rtcclient.client import RTCClient
from rtcclient.utils import setup_basic_logging
import os.path
import logging

def ensure_path_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='RTC Delta')
    if arguments["--logs"]:
        setup_basic_logging()
    else:
        logging.basicConfig(level=logging.CRITICAL)

    rtc_client = RTCClient(arguments["--url"],
                          arguments["--user"],
                          arguments["--pass"],
                          ends_with_jazz=arguments["--endsWithJazz"])
    ensure_path_exists(arguments["--beforePath"])
    ensure_path_exists(arguments["--afterPath"])
    work_item = rtc_client.getWorkitem(arguments["--workitem"]) # ,returned_properties="dc.ientifier,dc:title,rtc_cm:com.ibm.team.filesystem.workitems.change_set.com.ibm.team.scm.ChangeSet"
    print("%s : %s"% (work_item.identifier, work_item.title))
    changesets = work_item.getChangeSets()
    for changeset in changesets:
        print("Traversing %s" % changeset)
        for change in changeset.getChanges():
            print("Extracting before&after for change: %s" % change.comment)
            change.fetchBeforeStateFile(arguments["--beforePath"])
            change.fetchAfterStateFile(arguments["--afterPath"])
