import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for professional-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

# Load the data
seattle_data = pd.read_csv('seattle_rain.csv')
grr_data = pd.read_csv('grr_rain.csv')

# Add city labels
seattle_data['City'] = 'Seattle'
grr_data['City'] = 'Grand Rapids'

# Combine datasets
combined_data = pd.concat([seattle_data, grr_data], ignore_index=True)

# Calculate averages
seattle_avg = seattle_data['PRCP'].mean()
grr_avg = grr_data['PRCP'].mean()

print(f"Seattle Average: {seattle_avg:.4f} inches")
print(f"Grand Rapids Average: {grr_avg:.4f} inches")
print(f"Difference: {grr_avg - seattle_avg:.4f} inches")
print(f"Grand Rapids gets {((grr_avg - seattle_avg) / seattle_avg * 100):.1f}% more precipitation")

# ============================================================
# VISUALIZATION 1: Bar Chart - Average Daily Precipitation
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

cities = ['Seattle', 'Grand Rapids']
averages = [seattle_avg, grr_avg]
colors = ['#4A90E2', '#E85D75']

bars = ax.bar(cities, averages, color=colors, alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.4f}"',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_ylabel('Average Daily Precipitation (inches)', fontsize=12, fontweight='bold')
ax.set_title('Average Daily Precipitation Comparison', fontsize=14, fontweight='bold', pad=20)
ax.set_ylim(0, max(averages) * 1.15)

# Add a subtle grid
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('figure1_average_precipitation.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Figure 1 saved: Average Precipitation Bar Chart")

# ============================================================
# VISUALIZATION 2: Box Plot - Distribution Comparison
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Filter out zero values for better visualization of rainy days
seattle_rainy = seattle_data[seattle_data['PRCP'] > 0]['PRCP']
grr_rainy = grr_data[grr_data['PRCP'] > 0]['PRCP']

box_data = [seattle_rainy, grr_rainy]
bp = ax.boxplot(box_data, labels=['Seattle', 'Grand Rapids'], 
                patch_artist=True, widths=0.6,
                medianprops=dict(color='black', linewidth=2),
                boxprops=dict(facecolor='lightblue', alpha=0.7),
                whiskerprops=dict(linewidth=1.5),
                capprops=dict(linewidth=1.5))

# Color the boxes
colors = ['#4A90E2', '#E85D75']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_ylabel('Precipitation on Rainy Days (inches)', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Precipitation on Rainy Days', fontsize=14, fontweight='bold', pad=20)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('figure2_distribution_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Figure 2 saved: Distribution Box Plot")

# ============================================================
# VISUALIZATION 3: Precipitation Frequency Comparison
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate percentage of days with rain
seattle_rainy_days = (seattle_data['PRCP'] > 0).sum()
seattle_total_days = len(seattle_data)
seattle_pct = (seattle_rainy_days / seattle_total_days) * 100

grr_rainy_days = (grr_data['PRCP'] > 0).sum()
grr_total_days = len(grr_data)
grr_pct = (grr_rainy_days / grr_total_days) * 100

categories = ['Rainy Days', 'Dry Days']
seattle_values = [seattle_pct, 100 - seattle_pct]
grr_values = [grr_pct, 100 - grr_pct]

x = np.arange(len(categories))
width = 0.35

bars1 = ax.bar(x - width/2, seattle_values, width, label='Seattle', 
               color='#4A90E2', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax.bar(x + width/2, grr_values, width, label='Grand Rapids', 
               color='#E85D75', alpha=0.8, edgecolor='black', linewidth=1.5)

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_ylabel('Percentage of Days (%)', fontsize=12, fontweight='bold')
ax.set_title('Frequency of Rainy vs. Dry Days', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.legend(fontsize=11, loc='upper right')
ax.set_ylim(0, 105)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.set_axisbelow(True)

plt.tight_layout()
plt.savefig('figure3_rainy_days_frequency.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Figure 3 saved: Rainy Days Frequency")

# ============================================================
# VISUALIZATION 4: Summary Statistics Table Visual
# ============================================================
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('tight')
ax.axis('off')

# Calculate statistics
stats_data = {
    'Metric': [
        'Average Daily Precipitation',
        'Days with Rain',
        'Average on Rainy Days',
        'Maximum Daily Precipitation',
        'Total Days Measured'
    ],
    'Seattle': [
        f'{seattle_avg:.4f}"',
        f'{seattle_rainy_days} ({seattle_pct:.1f}%)',
        f'{seattle_rainy.mean():.4f}"',
        f'{seattle_data["PRCP"].max():.4f}"',
        f'{seattle_total_days}'
    ],
    'Grand Rapids': [
        f'{grr_avg:.4f}"',
        f'{grr_rainy_days} ({grr_pct:.1f}%)',
        f'{grr_rainy.mean():.4f}"',
        f'{grr_data["PRCP"].max():.4f}"',
        f'{grr_total_days}'
    ]
}

# Create DataFrame
stats_df = pd.DataFrame(stats_data)

# Create table
table = ax.table(cellText=stats_df.values, colLabels=stats_df.columns,
                cellLoc='center', loc='center', 
                colColours=['#E8E8E8', '#4A90E2', '#E85D75'],
                cellColours=[['white']*3]*len(stats_df))

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 2.5)

# Style header
for i in range(3):
    table[(0, i)].set_text_props(weight='bold', color='white')
    
# Style first column
for i in range(1, len(stats_df) + 1):
    table[(i, 0)].set_text_props(weight='bold', ha='left')
    table[(i, 0)].set_facecolor('#F5F5F5')

ax.set_title('Comprehensive Precipitation Statistics', 
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('reports/figure4_statistics_table.png', dpi=300, bbox_inches='tight')
plt.show()

print("✓ Figure 4 saved: Statistics Table")

# ============================================================
# Print Summary
# ============================================================
print("\n" + "="*60)
print("VISUALIZATION SUMMARY")
print("="*60)
print(f"✓ All 4 figures saved successfully to 'reports/' folder")
print(f"\n Key Findings:")
print(f"  • Grand Rapids: {grr_avg:.4f} inches/day average")
print(f"  • Seattle: {seattle_avg:.4f} inches/day average")
print(f"  • Difference: {grr_avg - seattle_avg:.4f} inches/day (Grand Rapids gets {((grr_avg - seattle_avg) / seattle_avg * 100):.1f}% more)")
print(f"  • Seattle has rain on {seattle_pct:.1f}% of days")
print(f"  • Grand Rapids has rain on {grr_pct:.1f}% of days")
print("="*60)
