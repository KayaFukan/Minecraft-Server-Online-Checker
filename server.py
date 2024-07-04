from mcstatus import JavaServer
import tkinter as tk

def check_server_status(server_address):
    server = JavaServer.lookup(server_address)
    try:
        status = server.status()
        return f"Sunucu açık! {status.players.online} oyuncu bağlı."
    except:
        return "Sunucu kapalı!"


def server(info):
    server_address = "thomas-pac.gl.joinmc.link"
    info = check_server_status(server_address)
    root = tk.Tk()
    root.title("Sunucu")
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (window_width / 2)
    y_coordinate = (screen_height / 2) - (window_height / 2)
    root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
    frame = tk.Frame(root)
    frame.pack(expand=True)
    label_url = tk.Label(frame, text=info, font=("Helvetica", 16, "bold"))
    label_url.pack(expand=True)
    root.mainloop()


if __name__ == "__main__":
    server("Sunucu Durumu")