"""RTC Delta

Usage:
  rtcdelta      --user=<username> --pass=<password> --url=<rtcUrl> --workitem=<id>  \r\n \
                [--endsWithJazz] [--logs]

Options:
  --user=<username>         Username, for RTC authentication.
  --pass=<password>         Password, for RTC authentication.
  --url=<rtcUrl>            RTC URL.
  --workitem=<id>           ID of the work item we want to analyze.
  --endsWithJazz            If your url ends with ccm, no neet to set to True.
  --logs                    If you want to see log lines in the console


Author:
  Marcio Marchini (marcio@BetterDeveloper.net)

"""

from docopt import docopt
from rtcclient.client import RTCClient
from rtcclient.utils import setup_basic_logging

if __name__ == '__main__':
    arguments = docopt(__doc__, version='RTC Delta')
    if arguments["--logs"]:
        setup_basic_logging()
    rtc_client = RTCClient(arguments["--url"],
                          arguments["--user"],
                          arguments["--pass"],
                          ends_with_jazz=arguments["--endsWithJazz"])
    #prj_areas = rtc_client.getProjectAreas()
    #print (prj_areas)
    work_item = rtc_client.getWorkitem(arguments["--workitem"]) # ,returned_properties="dc.ientifier,dc:title"
    print("%s : %s"% (work_item.identifier, work_item.title))
    changesets = work_item.getChangeSets()
    for changeset in changesets:
        print (changeset)
