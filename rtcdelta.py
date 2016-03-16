"""RTC Delta

Usage:
  rtcdelta      --user=<username> --pass=<password> --url=<rtcUrl> \r\n \
                [--endsWithJazz]

Options:
  --user=<username>         Username, for RTC authentication.
  --pass=<password>         Password, for RTC authentication.
  --url=<rtcUrl>            RTC URL.


Author:
  Marcio Marchini (marcio@BetterDeveloper.net)

"""


from docopt import docopt
from rtcclient.utils import setup_basic_logging
from rtcclient.client import RTCClient

if __name__ == '__main__':
    arguments = docopt(__doc__, version='RTC Delta')
    # you can remove this if you don't need logging
    # default debug logging for console output
    setup_basic_logging()
    # if your url ends with ccm, set ends_with_jazz to False
    # refer to issue #68 for detailed explanation
    rtcClient = RTCClient(arguments["--url"],
                          arguments["--user"],
                          arguments["--pass"],
                          ends_with_jazz=arguments["--endsWithJazz"])
    prj_areas = rtcClient.getProjectAreas()
    print (prj_areas)