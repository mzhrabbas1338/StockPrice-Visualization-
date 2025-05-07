import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.colors as mcolors

# Load the data
file_path = r'C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\FINAL STOCK DATA.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Set the date as the index for easier manipulation
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Load stock images (logos)
stock_images = {
    "Vstock": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\Visa Stock.png",
    "TSLA": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\Tesla.png",
    "ORCL": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\ORCL.png",
    "NVDA": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\NVDA.png",
    "NFLX": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\NFLX.jpeg",
    "MSFT": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\MSFT.png",
    "Meta": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\Meta.png",
    "JPM": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\JPM.png",
    "INTC": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\INTC.png",
    "IBM": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\IBM.png",
    "APPLE": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\AAPL.png",
    "AMAZON": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\AMZN.png",
    "BOA": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\BOA.png",
    "Cisco": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\Cisco.png",
    "GOOGLE": r"C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\Icons\Google.png"
}

# Assign a unique color to each stock using matplotlib's colors
colors = list(mcolors.TABLEAU_COLORS.keys())  # Get a list of predefined colors
stock_colors = {stock: colors[i % len(colors)] for i, stock in enumerate(stock_images)}

# Initialize the plot with higher DPI for better quality
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

def get_image(path):
    """ Helper function to load an image from a path and return it as an OffsetImage """
    img = mpimg.imread(path)
    return OffsetImage(img, zoom=0.1)

# Define the update function for animation
def update(num):
    ax.clear()
    data = df.iloc[num].sort_values(ascending=False)[:10]  # Top 10 stocks for the date

    # Plot the bars with their respective colors and add gridlines
    bars = ax.barh(data.index, data.values, color=[stock_colors.get(stock, 'gray') for stock in data.index], edgecolor='black')

    # Annotate each bar with the stock image (logo)
    for i, (stock, value) in enumerate(zip(data.index, data.values)):
        if stock in stock_images:
            img = get_image(stock_images[stock])
            ab = AnnotationBbox(img, (value, i), frameon=False, xybox=(50, 0), xycoords='data', boxcoords="offset points", pad=0)
            ax.add_artist(ab)

    # Add gridlines for better readability
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)

    # Set the title, labels, and limits
    ax.set_title(f"Stock Prices on {df.index[num].strftime('%Y-%m-%d')}", fontsize=16)
    ax.set_xlim([0, data.max() + 10])
    ax.set_xlabel("Stock Price in $", fontsize=12)
    ax.set_ylabel("Stocks", fontsize=12)

    # Invert y-axis so highest values are on top
    ax.invert_yaxis()

# Create the animation with smoother transitions
ani = FuncAnimation(fig, update, frames=len(df), repeat=False, interval=200)

# Save the animation as MP4 with better quality (higher DPI and bitrate)
#output_path = r'C:\Users\SMART TECH\OneDrive - Higher Education Commission\Desktop\RaceBarChart\stock_animation.mp4'
#ani.save(output_path, writer='ffmpeg', fps=3, bitrate=5000, dpi=300, codec="libx264")
# Show the plot
plt.show()
