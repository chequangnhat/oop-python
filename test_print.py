from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print
from rich.layout import Layout

from datetime import datetime

table = Table(title="table title", show_header=False,show_lines=True, expand=True,pad_edge=False)

table.add_column("col1", style="cyan")
table.add_column("col2", style="cyan")

table.add_row("row1sd")
table.add_row("row2","hjh")

table2 = Table(show_header=False,show_lines=True, expand=True,pad_edge=False)
table2.add_column("col1", style="cyan")
table2.add_row("row1sd")
console = Console()

console.print(table)
console.print(table2)

############################################################

# layout = Layout()

# layout.split_row(
#     Layout(name="right"),
#     Layout(name="left")
# )
# print(layout)

############################################################

# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))