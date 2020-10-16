###################################################################
#           Copyright (c) 2016 by TAOS Technologies, Inc.
#                     All rights reserved.
#
#  This file is proprietary and confidential to TAOS Technologies.
#  No part of this file may be reproduced, stored, transmitted,
#  disclosed or used in any form or by any means other than as
#  expressly provided by the written permission from Jianhui Tao
#
###################################################################

# -*- coding: utf-8 -*-

import sys
import taos
from util.log import *
from util.cases import *
from util.sql import *
import numpy as np


class TDTestCase:
    def init(self, conn, logSql):
        tdLog.debug("start to execute %s" % __file__)
        tdSql.init(conn.cursor())

        self.rowNum = 10
        self.ts = 1537146000000
        
    def run(self):
        tdSql.execute("use db")

        intData = []        
        floatData = []

        for i in range(self.rowNum):
            intData.append(i + 1)            
            floatData.append(i + 0.1)                        

        # twa verifacation 
        tdSql.error("select twa(ts) from test")
        tdSql.error("select twa(ts) from test1")

        tdSql.error("select twa(col1) from test")
        tdSql.error("select twa(col1) from test1")

        tdSql.error("select twa(col2) from test")
        tdSql.error("select twa(col2) from test1")

        tdSql.error("select twa(col3) from test")
        tdSql.error("select twa(col3) from test1")

        tdSql.error("select twa(col4) from test")
        tdSql.error("select twa(col4) from test1")

        tdSql.error("select twa(col5) from test")
        tdSql.error("select twa(col5) from test1")

        tdSql.error("select twa(col6) from test")
        tdSql.error("select twa(col6) from test1")        

        tdSql.error("select twa(col7) from test")
        tdSql.error("select twa(col7) from test1")

        tdSql.error("select twa(col8) from test")
        tdSql.error("select twa(col8) from test1")

        tdSql.error("select twa(col9) from test")
        tdSql.error("select twa(col9) from test1")

        tdSql.error("select twa(col1) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col1) from test1 where ts > %d" % self.ts)

        tdSql.error("select twa(col2) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col2) from test1 where ts > %d" % self.ts)

        tdSql.error("select twa(col3) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col3) from test1 where ts > %d" % self.ts)

        tdSql.error("select twa(col4) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col4) from test1 where ts > %d" % self.ts)
            
        tdSql.error("select twa(col5) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col5) from test1 where ts > %d" % self.ts)

        tdSql.error("select twa(col6) from test where ts > %d" % self.ts)
        tdSql.error("select twa(col6) from test1 where ts > %d" % self.ts)

        tdSql.error("select twa(col1) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col1) from test1 where ts < %d" % (self.ts + self.rowNum))

        tdSql.error("select twa(col2) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col2) from test1 where ts < %d" % (self.ts + self.rowNum))

        tdSql.error("select twa(col3) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col3) from test1 where ts < %d" % (self.ts + self.rowNum))

        tdSql.error("select twa(col4) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col4) from test1 where ts < %d" % (self.ts + self.rowNum))

        tdSql.error("select twa(col5) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col5) from test1 where ts < %d" % (self.ts + self.rowNum))

        tdSql.error("select twa(col6) from test where ts < %d" % (self.ts + self.rowNum))
        tdSql.error("select twa(col6) from test1 where ts < %d" % (self.ts + self.rowNum))
        
        tdSql.query("select twa(col1) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))
        tdSql.query("select twa(col1) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

        tdSql.query("select twa(col2) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))
        tdSql.query("select twa(col2) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

        tdSql.query("select twa(col3) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))
        tdSql.query("select twa(col3) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

        tdSql.query("select twa(col4) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum)) 
        tdSql.query("select twa(col4) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

        tdSql.query("select twa(col5) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum)) 
        tdSql.query("select twa(col5) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

        tdSql.query("select twa(col6) from test where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))         
        tdSql.query("select twa(col6) from test1 where ts > %d  and ts < %d" % (self.ts, self.ts + self.rowNum))

    def stop(self):
        tdSql.close()
        tdLog.success("%s successfully executed" % __file__)

tdCases.addWindows(__file__, TDTestCase())
tdCases.addLinux(__file__, TDTestCase())
