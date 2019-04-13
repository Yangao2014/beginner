#!user/bin/env python
# -*- coding?:utf-8 -*-
# @time   :  
# @Author :Amber
# File    :.py
from pytube import Playlist
pl = Playlist("https://www.youtube.com/channel/UC9FZPSsbq1E2ny9WW6pnbpg/playlists")
pl.download_all("/path/to/directory/DrSuessEpisodes")
