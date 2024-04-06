import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import random
import string
from ttkthemes import ThemedStyle

class M3U8Player:
    def __init__(self, root):
        self.root = root
        self.root.title("M3U8 Player")
        self.root.geometry("230x380")
        #self.root.iconbitmap("img/icon32png")
        # PNG dosyasını yükle
        self.icon_image = tk.PhotoImage(file="img/icon32.png")

        # Başlık çubuğundaki simgeyi değiştir
        root.tk.call('wm', 'iconphoto', root._w, self.icon_image)
        
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)

        self.playlist = {}

        self.default_playlist = {
            "Bein Sports 1": "https://sette.42c65aec57cd39f.shop/selcuksports/www.selcuksportshd1178.xyz/601/playlist.m3u8",
            "Bein Sports 1": "https://tre.42c65aec57cd39f.shop/selcuksports/www.selcuksportshd1178.xyz/601/playlist.m3u8",
            "Bein Sports 2": "https://cinque.6a0ec8ce41cae2c.shop/selcuksports/www.selcuksportshd1181.xyz/602/playlist.m3u8",
            "Bein Sports 3": "https://quattro.6a0ec8ce41cae2c.shop/selcuksports/www.selcuksportshd1181.xyz/603/playlist.m3u8",
            "Bein Sports 4": "https://cinque.6a0ec8ce41cae2c.shop/selcuksports/www.selcuksportshd1181.xyz/604/playlist.m3u8",
            "Bein Sports 5": "https://tre.6a0ec8ce41cae2c.shop/selcuksports/www.selcuksportshd1181.xyz/705/playlist.m3u8",
            "Bein Sports 1 HD": "https://cinque.42c65aec57cd39f.shop/q/www.selcuksportshd1178.xyz/601/f.acdwatercn.shop/chunklist_hd.m3u8",
            "Bein Sports 1 HD": "https://sette.42c65aec57cd39f.shop/q/www.selcuksportshd1178.xyz/601/e.acdwatercn.shop/chunklist_hd.m3u8",
            "Bein Sports 2 HD": "https://tre.6a0ec8ce41cae2c.shop/q/www.selcuksportshd1181.xyz/602/f.acdwatercn.shop/chunklist_hd.m3u8",
            "Bein Sports 3 HD": "https://sette.6a0ec8ce41cae2c.shop/q/www.selcuksportshd1181.xyz/603/b.acdwatercn.shop/chunklist_hd.m3u8",
            "Bein Sports 4 HD": "https://due.6a0ec8ce41cae2c.shop/q/www.selcuksportshd1181.xyz/604/f.acdwatercn.shop/chunklist_hd.m3u8",
            "Bein Sports 5 HD": "https://sei.6a0ec8ce41cae2c.shop/q/www.selcuksportshd1181.xyz/705/b.acdwatercn.shop/chunklist_hd.m3u8",
            "Kanal D 720P":"https://demiroren.daioncdn.net/kanald/kanald_720p.m3u8?e=1712275562&reqid=cf8df5f109ffde94cf11859b8c1b597e&st=RCtWrF82MypAO5M8TtwPWA&tmode=1&uid=7158165202298013938&userid=&sid=6akd1bj9wwej&app=4caf18fc-b51a-40c1-94d1-2940555a42f9&ce=3",
            "Kanal D 720P":"https://demiroren.daioncdn.net/kanald/kanald_720p.m3u8?e=1712275467&reqid=0acb527a4c0f58740a03d00451216fdf&st=4HVIK-GgpHduF6EcT9NwoA&tmode=1&uid=7158165202298013938&userid=&sid=6akcwex98llq&app=4caf18fc-b51a-40c1-94d1-2940555a42f9&ce=3",
            "Qaf TV (1080p)": "https://mn-nl.mncdn.com/qaf/live/playlist.m3u8",
            "Qmusic HD": "https://dpp-qmusicnl-live.akamaized.net/streamx/QmusicNL_720p.m3u8",
            "RMTV": "http://transcoder1.bitcare.eu/streaming/rimextv/rmtv.m3u8",
            "Rehber TV": "https://yayin30.haber100.com/live/rehbertv/playlist.m3u8",
            "SPIRIT TV MUSIC": "https://cdnlive.myspirit.tv/LS-ATL-43240-2/tracks-v1a1/mono.m3u8",
            "STAR TV SD": "https://dogus-live.daioncdn.net/startv/playlist.m3u8",
            "Saryarga": "https://stream.kaztrk.kz/regional/karagandytv/index.m3u8",
            "Show Turk": "https://showturk.blutv.com/blutv_showturk2/live.m3u8",
            "Sieng Khaen Lao": "https://livefta.malimarcdn.com/ftaedge00/vlctemple.sdp/playlist.m3u8",
            "Sinop Yildiz TV": "https://s01.vpis.io/sinopyildiz/sinopyildiz.m3u8",
            "Star TV": "https://dogus-live.daioncdn.net/startv/startv_720p.m3u8",
            "Star TV (720p)": "https://dogus-live.daioncdn.net/startv/startv.m3u8",
            "TBMM TV": "https://meclistv-live.ercdn.net/meclistv/meclistv_720p.m3u8",
            "TBMM TV (720p)": "https://meclistv-live.ercdn.net/meclistv/meclistv.m3u8",
            "TRT 2": "https://trt2.blutv.com/blutv_trt2/live.m3u8",
            "TRT 4K": "http://96a6b6a3.ottolok.net/iptv/URFPS4QVV53QPF/4001/index.m3u8",
            "TRT ARABi": "http://tv-trtarabi.live.trt.com.tr/master.m3u8",
            "TRT AVAZ": "https://tv-trtavaz.medya.trt.com.tr/master_720.m3u8",
            "TRT Cocuk": "https://tv-trtcocuk.live.trt.com.tr/master.m3u8",
            "TRT Kürdi": "https://tv-trtkurdi.medya.trt.com.tr/master_720.m3u8",
            "TRT MUZiK": "https://tv-trtmuzik.medya.trt.com.tr/master_720.m3u8",
            "TRT Türk": "https://tv-trtturk.medya.trt.com.tr/master_720.m3u8",
            "TRT WORLD HD-TR (720p)": "http://tv-trtworld.live.trt.com.tr/master_720.m3u8",
            "TRT World": "https://tv-trtworld.live.trt.com.tr/master.m3u8",
            "TRT Çocuk": "http://tv-trtcocuk.live.trt.com.tr/master_720.m3u8",
            "TURHAL WEB TV": "http://cdn-turhalwebtv.yayin.com.tr/turhalwebtv/turhalwebtv/chunklist_w1702401498.m3u8",
            "TV 1 (720p)": "https://edge1.socialsmart.tv/tv1/bant1/playlist.m3u8",
            "TV 100 (720p)": "https://tv100.blutv.com/blutv_tv100_live/live.m3u8",
            "TV 264 (1080p)": "https://b01c02nl.mediatriple.net/videoonlylive/mtdxkkitgbrckilive/broadcast_5ee244263fd6d.smil/playlist.m3u8",
            "TV 264 Sakarya": "https://mc1.mediatriple.net/videoonlylive/mtdxkkitgbrckilive/broadcast_5ee244263fd6d.smil/playlist.m3u8",
            "TV 41 (720p)": "http://stream.taksimbilisim.com:1935/tv41/smil:tv41.smil/playlist.m3u8",
            "TV 41 m3u8 taksimbilisim": "http://stream.taksimbilisim.com:1935/tv41/bant1/TV41.m3u8",
            "TV 52": "http://stream.taksimbilisim.com:1935/tv52/smil:tv52.smil/iptvdelisi.m3u8",
            "TV 52 m3u8 taksimbilisim": "http://stream.taksimbilisim.com:1935/tv52/bant1/TV52.m3u8",
            "TV4": "https://turkmedya-live.ercdn.net/tv4/tv4_720p.m3u8",
            "TV52": "http://stream.taksimbilisim.com:1935/tv52/smil:tv52.smil/playlist.m3u8",
            "Tarim TV (1080p)": "https://content.tvkur.com/l/c7e1da7mm25p552d9u9g/master.m3u8",
            "Tatlises TV (720p)": "https://live.artidijitalmedya.com/artidijital_tatlisestv/tatlisestv/playlist.m3u8",
            "Tek Rumeli TV (576p)": "https://edge1.socialsmart.tv/tekrumelitv/bant1/playlist.m3u8",
            "Tempo TV": "https://live.artidijitalmedya.com/artidijital_tempotv/tempotv/playlist.m3u8",
            "Teve2 (1080p)": "https://teve2vod.duhnet.tv/S12/HLS_VOD/382843_2e5b/index.m3u8",
            "Tivi 6 (720p)": "https://live.artidijitalmedya.com/artidijital_tivi6/tivi6/playlist.m3u8",
            "Ton TV (720p)": "https://live.artidijitalmedya.com/artidijital_tontv/tontv/playlist.m3u8",
            "Turhal Web TV": "http://cdn-turhalwebtv.yayin.com.tr/turhalwebtv/turhalwebtv/HasBahCa_w1702401498.m3u8",
            "TürkHaber (720p)": "https://edge1.socialsmart.tv/turkhaber/bant1/playlist.m3u8",
            "UR FANATiK TV YEDEK": "https://edge1.socialsmart.tv/urfanatiktv/bant1/chunks.m3u8",
            "UYGUR TV NEWS": "https://592f1881b3d5f.streamlock.net:1443/santraltv_742/santraltv_742/chunklist_w1333397898.m3u8",
            "VOX AFRICA": "https://1494836162.rsc.cdn77.org/LS-PRG-59570-1/tracks-v1a1/mono.m3u8",
            "VTV (720p)": "https://live.artidijitalmedya.com/artidijital_kanalv/kanalv/playlist.m3u8",
            "Vizyon 58 TV (720p)": "https://live.artidijitalmedya.com/artidijital_vizyon58/vizyon58/playlist.m3u8",
            "tivi TÜRK": "https://stream.tiviturk.de/live/tiviturk.m3u8",
            "Çay TV": "https://edge1.socialsmart.tv/caytv/bant1/chunks.m3u8",
            "Üniversite TV": "https://vdo.digitalbox.xyz:3986/live/unitvlive.m3u8"
        }


        self.style = ThemedStyle(self.root)
        self.style.theme_use('clearlooks')  # Modern bir görünüm için varsayılan tema

        self.create_widgets()
        self.load_default_playlist()

    def search_playlist(self):
        query = self.entry_search.get().lower()
        self.listbox.delete(0, tk.END)
        for index, (title, path) in enumerate(self.playlist.items(), start=1):
            if query in title.lower():
                self.listbox.insert(tk.END, f"{index}. {title} | {path}")

    def load_default_playlist(self):
        self.playlist = self.default_playlist
        self.update_listbox()

    def create_widgets(self):

        # İkinci çerçeve oluştur
        self.frame3 = ttk.Frame(self.root)
        self.frame3.pack(pady=10)

        # Üçüncü çerçevedeki giriş kutusu ve butonu yerleştir
        self.entry_search = ttk.Entry(self.frame3, width=25)
        self.entry_search.pack(side=tk.LEFT, pady=5, padx=5)

        #self.entry_search.insert(0, "Arama:")

        self.search_button = ttk.Button(self.frame3, text="Ara", command=self.search_playlist)
        self.search_button.pack(side=tk.LEFT, pady=5)


        self.entry = ttk.Entry(self.root, width=35)
        self.entry.pack(pady=5)

        self.entry.insert(0, "M3U8 Başlık | URL .m3u8")

      # Çerçeve oluştur
        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=10)

        # Butonları çerçevenin içine yerleştir
        self.add_button = ttk.Button(self.frame, text="Ekle", command=self.add_playlist)
        self.add_button.grid(row=0, column=0, padx=5)

        self.browse_button = ttk.Button(self.frame, text="Gözat", command=self.browse_playlist)
        self.browse_button.grid(row=0, column=1, padx=5)

        self.clear_button = ttk.Button(self.frame, text="Temizle", command=self.clear_listbox)
        self.clear_button.grid(row=0, column=2, padx=5)

        self.listbox_frame = ttk.Frame(self.root)
        self.listbox_frame.pack(pady=5)

        self.listbox_scrollbar_y = ttk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        self.listbox_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_scrollbar_x = ttk.Scrollbar(self.listbox_frame, orient=tk.HORIZONTAL)
        self.listbox_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.listbox = tk.Listbox(self.listbox_frame, width=33, height=10, yscrollcommand=self.listbox_scrollbar_y.set, xscrollcommand=self.listbox_scrollbar_x.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox_scrollbar_y.config(command=self.listbox.yview)
        self.listbox_scrollbar_x.config(command=self.listbox.xview)

         # İkinci çerçeve oluştur
        self.frame2 = ttk.Frame(self.root)
        self.frame2.pack(pady=10)

         # İkinci çerçevedeki butonları yerleştir
        self.play_button = ttk.Button(self.frame2, text="Oynat", command=self.open_browser)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.save_button = ttk.Button(self.frame2, text="Listeyi Kaydet", command=self.save_playlist)
        self.save_button.pack(side=tk.LEFT, padx=5)

    def clear_listbox(self):
        self.listbox.delete(0, tk.END)
        self.playlist.clear()

    def add_playlist(self):
        m3u8_path = self.entry.get()
        if m3u8_path:
            title = m3u8_path #.split("/")[-1]
            self.playlist[title] = m3u8_path
            self.update_listbox()

    def browse_playlist(self):
        file_path = filedialog.askopenfilename(title="Dosya Seç", filetypes=(("M3U8 Files", "*.m3u8"), ("Text Files", "*.txt"), ("All files", "*.*")))
        if file_path:
            with open(file_path, "r", encoding="latin-1") as file:
                title = None
                m3u8_link = None
                if file_path.endswith(".m3u8"):
                    with open(file_path, "r", encoding="utf-8") as m3u8_file:
                        for line in m3u8_file:
                            line = line.strip()
                            if line.startswith("#EXTINF:"):
                                if title and m3u8_link:
                                    self.playlist[title] = m3u8_link
                                title = None
                                m3u8_link = None
                                title = line.split(",")[-1]
                            elif line.startswith("http"):
                                m3u8_link = line
                    if title and m3u8_link:
                        self.playlist[title] = m3u8_link
                elif file_path.endswith(".txt"):
                    for line in file:
                        line = line.strip()
                        if line:
                            parts = line.split("|")
                            if len(parts) == 2:
                                title = parts[0]
                                m3u8_link = parts[1]
                                self.playlist[title] = m3u8_link
            self.update_listbox()

            
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for index, (title, path) in enumerate(self.playlist.items(), start=1):
            self.listbox.insert(tk.END, f"{index}. {title}  |  {path}")

    def open_browser(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index[0])
            selected_title = selected_item.split('|')[0].strip()  # Extracting the title part
            selected_m3u8_path_url = selected_item.split('|')[1].strip()  # Extracting the title part
            selected_m3u8_path = selected_m3u8_path_url
            if selected_m3u8_path:  
                chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                browser_url = f"chrome-extension://gijhpnmjcpbddpedmmdihijogkkejfgj/player.html#{selected_m3u8_path}"
                print("Browser URL:", browser_url)
                try:
                    subprocess.Popen([chrome_path, browser_url])
                    print("Browser opened successfully.")
                except Exception as e:
                    messagebox.showerror("Hata", "Tarayıcı başlatılamadı.")
                    print("Error:", e)

    def save_playlist(self):
        if self.playlist:
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "_list.txt"
            with open(random_name, "w") as file:
                for index, (title, path) in enumerate(self.playlist.items(), start=1):
                    file.write(f"{index}. {title}|{path}\n")
            messagebox.showinfo("Başarılı", "Liste başarıyla kaydedildi.")

if __name__ == "__main__":
    root = tk.Tk()
    app = M3U8Player(root)
    root.mainloop()
