s1=[r'''magnet:?xt=urn:btih:220CF4AE60C25E32E675C8C714EA479D29A70A18&dn=Vikings+S01+Complete+Season+1+EXTENDED+BluRay+720p+x265+HEVC&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Fzer0day.ch%3A1337&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce''']
import libtorrent as lt
import time
import sys
for source in s1:
  ses = lt.session()
  ses.listen_on(6881, 6891)
  params = {"save_path": "./"}
  if isinstance(source, str):h = lt.add_magnet_uri(ses, source, params)
  else:
    params["ti"] = lt.torrent_info(list(source.keys())[0])
    h = ses.add_torrent(params)
    print("starting", h.name())
  print("starting", h.name())
  while not h.is_seed():
    s = h.status()
    state_str = ["queued","checking","downloading metadata","downloading","finished","seeding","allocating","checking fastresume"]
    print(" \r%.2f%% of %.2fMB, %.1f, %.1f , %d, %s " % (s.progress * 100,s.total_wanted/1024.0/1024.0,s.download_rate / 1000,s.upload_rate / 1000,s.num_peers,state_str[s.state],))
    sys.stdout.flush()
    time.sleep(1)
  print(h.name(), "complete")
