#!/usr/bin/env python3
import argparse,datetime,os
from xml.sax.saxutils import quoteattr
def main():
 p=argparse.ArgumentParser();p.add_argument("--out",required=True);p.add_argument("--content-id",required=True);p.add_argument("files",nargs="+");a=p.parse_args()
 fs=[x.replace("\\","/") for x in a.files]; ts=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 x=['<?xml version="1.0"?>','<psproject xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" fmt="gp4" version="1000">','<volume><volume_type>pkg_ps4_app</volume_type><volume_id>PS4VOLUME</volume_id><volume_ts>'+ts+'</volume_ts><package content_id='+quoteattr(a.content_id)+' passcode="00000000000000000000000000000000" storage_type="digital50" app_type="full" /><chunk_info chunk_count="1" scenario_count="1"><chunks><chunk id="0" layer_no="0" label="Chunk #0" /></chunks><scenarios default_id="0"><scenario id="0" type="sp" initial_chunk_count="1" label="Scenario #0">0</scenario></scenarios></chunk_info></volume>','<files img_no="0">']
 for f in fs:x.append('<file targ_path='+quoteattr(f)+' orig_path='+quoteattr(f)+' />')
 x.append('</files><rootdir><dir targ_name="sce_sys"><dir targ_name="about"><dir targ_name="right.sprx" /></dir><dir targ_name="icon0.png" /><dir targ_name="param.sfo" /></dir><dir targ_name="eboot.bin" /></rootdir></psproject>')
 open(a.out,"w").write("\n".join(x)+"\n")
if __name__=="__main__":main()
