"""RTC Delta

Usage:
  rtcdelta      --user=<username> --pass=<password> --url=<rtcUrl> --workitem=<id>  --beforePath=<beforePath> --afterPath=<afterPath> \r\n \
                [--endsWithJazz] [--logs] [--children]

Options:
  --user=<username>         Username, for RTC authentication.
  --pass=<password>         Password, for RTC authentication.
  --url=<rtcUrl>            RTC URL.
  --workitem=<id>           ID of the work item we want to analyze.
  --beforePath=<beforePath> Path into where perform the checkout of the file before the changes
  --afterPath=<afterPath>   Path into where perform the checkout of the file after the changes
  --endsWithJazz            If your url ends with ccm, no neet to set to True.
  --logs                    If you want to see log lines in the console
  --children                If you want to get children changes


Author:
  Marcio Marchini (marcio@BetterDeveloper.net)

"""

import logging
from docopt import docopt
from rtcclient.client import RTCClient
from rtcclient.utils import setup_basic_logging
import os.path

def ensure_path_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_changes(changesets):
    if not changesets:
        return

    for changeset in changesets:
        print("Traversing %s" % changeset)
        for change in changeset.getChanges():
            print("Extracting before&after for change: %s" % change.comment)
            change.fetchBeforeStateFile(arguments["--beforePath"])
            change.fetchAfterStateFile(arguments["--afterPath"])


def get_children(workitem):
    print("Getting children_list of %s : %s"% (workitem.identifier, workitem.title))
    workitem_list = [workitem]
    children_list = workitem.getChildren()
    if not children_list:
        return workitem_list

    for children in children_list:
        workitem_list += get_children(children)

    return workitem_list


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
    workitem = rtc_client.getWorkitem(arguments["--workitem"]) # ,returned_properties="dc.ientifier,dc:title,rtc_cm:com.ibm.team.filesystem.workitems.change_set.com.ibm.team.scm.ChangeSet"
    if arguments['--children']:
        for children in get_children(workitem):
            print("%s : %s"% (children.identifier, children.title))
            get_changes(children.getChangeSets())
    else:
        print("%s : %s"% (workitem.identifier, workitem.title))
        get_changes(workitem.getChangeSets())
