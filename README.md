# rtcdelta
Delta on top of IBM RTC

## How to run

The snippet below will extract the original sources for the files that were changed (in the changesets of the --workitem)
and put them under --beforePath. It will also get the sources after the changes and put them under --afterPath.

```
python rtcdelta.py --user=james.bond --pass=abcd1234 --url=https://clm.unj.foo.com/ccm/ --workitem=35792 --beforePath=/Users/mqm/Downloads/rtc/before --afterPath=/Users/mqm/Downloads/rtc/after
```

Note that you can combine this utility with https://github.com/sglebs/udbcmp and compute how specific metrics changed.

#### Thank you!

Special thanks to [Softplan](http://www.softplan.con.br) for sponsoring this project/experiment. In particular, Anderson Soffa for the support.
