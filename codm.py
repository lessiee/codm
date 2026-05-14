import sys
import os
import time

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.align import Align
    from rich.text import Text
    from rich import box
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rich"])
    from rich.console import Console
    from rich.panel import Panel
    from rich.align import Align
    from rich.text import Text
    from rich import box

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    banner = r"""
     ██████╗ ██████╗ ██████╗ ███╗   ███╗
    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║
    ██║     ██║   ██║██║  ██║██╔████╔██║
    ██║     ██║   ██║██║  ██║██║╚██╔╝██║
    ╚██████╗╚██████╔╝██████╔╝██║ ╚═╝ ██║
     ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝
    """
    console.print(Align.center(Text(banner, style="bold #89CFF0")))
    console.print(Align.center(Text("⚡ MAINTENANCE MODE ⚡", style="#B0E0E6")))
    console.print(Align.center(Text("─" * 30, style="#4682B4")))
    console.print()

    message = (
        "[yellow]🔧 The Call of Duty Mobile Account Checker is currently under maintenance.[/yellow]\n\n"
        "[white]We're performing essential updates to improve accuracy and speed.\n"
        "Please check back in a few hours.[/white]\n\n"
        "[dim]We apologize for any inconvenience. Thank you for your patience.[/dim]\n\n"
        "[cyan]In the meantime, you can use other available tools from the main menu.[/cyan]"
    )

    panel = Panel(
        Align.center(message, vertical="middle"),
        border_style="bright_yellow",
        box=box.ROUNDED,
        width=70,
        padding=(2, 3)
    )
    console.print(Align.center(panel))
    console.print()

    footer = Panel(
        Align.center("[dim]Developed by @rrielqt[/dim]"),
        border_style="#4682B4",
        box=box.ROUNDED,
        width=70,
        padding=(0, 1)
    )
    console.print(Align.center(footer))

    console.print("\n[green]Press Enter to return to loader menu...[/green]")
    input()
    sys.exit(0)

if __name__ == "__main__":
    main()