s1=[r'''magnet:?xt=urn:btih:C0F1FCEC29E356C4F3215ED5BBECF8DA35525677&dn=Project+CARS+3-CODEX&tr=udp%3A%2F%2F9.rarbg.me%3A2720%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2800%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce''']
import libtorrent as lt
import time
import sys
for source in s1:
  ses = lt.session()
  ses.listen_on(6881, 6891)
  params = {"save_path": "./torrent"}
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
