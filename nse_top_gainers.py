from lxml import html
import requests
import time
import os,sys
import getpass
c=os.getenv('SystemDrive')
u=getpass.getuser()
logy='%s\Users\%s\Desktop\NSE_STOCK_MONITOR.txt'%(c,u)
f=open(logy,'a')

def mina():    
 while 1:
    try:
        y=open(logy,'a')
        try:
            page = requests.get('https://www.nse.co.ke/')
        except Exception as e:
        
            y.write('\nFailed to connect to NSE.\nCheck your INTERNET CONNECTION and try again')
            y.close()
            time.sleep(10*60)
            mina()
    
        y.write('\n'*2+'-'*90+'\nTOP GAINERS'+'\n'*2+'\n'+time.ctime())
    
        tree = html.fromstring(page.content)

        p= tree.xpath('//span[@class="uchange"]/text()')
        q=tree.xpath('//td[@class="itemt"]/text()')
        w=tree.xpath('//td[@class="itemr"]/text()')
        i=-1
        y.write('\n{0:10} --- {1:10} --- {2:10}\n'.format('STOCK','PRICE','CHANGE(%)'))

        while i<(len(q)-1):
            i=i+1
            try:
                y.write('\n{0:10} --- {1:10} --- {2:10}'.format(q[i],w[i],p[i]+' %'))
            except Exception as e:
                try:
                    y.write('\n{0:10} --- {1:10} ---    -'.format(q[i],w[i]))
                except Exception as e:
                    time.sleep(0)
        page2=requests.get('https://www.nse.co.ke/market-statistics/equity-statistics.html?view=statistics')
        tree2=html.fromstring(page2.content)
        p1= tree2.xpath('//td[@class="itemt"]/text()')
        q1=tree2.xpath('//td[@class="tprice"]/text()')
        r=tree2.xpath('//span[@class="uchange"]/text()')

        y.write('\n'*2+'-'*90)
        y.write('\n{0:65} --- {1:10} --- {2:10}\n'.format('COMPANY','PRICE','% INCREASE'))

        g=-1
        while g<(len(p1)-1):
            g=g+1
            try:
                y.write('\n{0:65} --- {1:10} --- {2:10}'.format(p1[g],q1[g],r[g]+' %'))
                y.write('\n'+'-'*90)
            except Exception as e:
                try:
                    y.write('\n{0:65} --- {1:10} ---   -'.format(p1[g],q1[g]))
                    y.write('\n'+'-'*90)
                except Exception as e:
                    time.sleep(0)
        time.sleep(3*60)
        y.write('\n')
        y.close()
    except Exception as e:
        time.sleep(3*60)
        exit

mina()
