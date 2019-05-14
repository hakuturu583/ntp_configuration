#!/usr/bin/env python
import os
import rospy
from time import ctime
import ntplib

def setTime(ntp_server_address,sudo_password):
    c = ntplib.NTPClient()
    response = c.request(ntp_server_address, version=3)
    now=ctime(response.tx_time)
    now_year = now[20:24]
    now_day = now[8:10]
    now_month = now[4:7]
    if now_month=="Jan":
        now_month=1
    if now_month=="Feb":
        now_month=2
    if now_month=="Mar":
        now_month=3
    if now_month=="Apr":
        now_month=4
    if now_month=="May":
        now_month=5
    if now_month=="Jun":
        now_month=6
    if now_month=="Jul":
        now_month=7
    if now_month=="Aug":
        now_month=8
    if now_month=="Sep":
        now_month=9
    if now_month=="Oct":
        now_month=10
    if now_month=="Nov":
        now_month=11
    if now_month=="Dec":
        now_month=12
    now_time = now[11:19]
    command = ("date -s"+" "+"'"+str(now_year)+"-"+str(now_month)+"-"+str(now_day)+" "+str(now_time)+"'")
    p = os.system('echo %s|sudo -S %s' % (sudo_password, command))

if __name__ == "__main__":
    rospy.init_node('ntp_configuration', anonymous=True)
    sudo_password = rospy.get_param(rospy.get_name()+"/sudo_password")
    ntp_server_address = rospy.get_param(rospy.get_name()+"/ntp_server_address")
    rate = rospy.Rate(0.01)
    while not rospy.is_shutdown():
        setTime(ntp_server_address,sudo_password)
        rate.sleep()