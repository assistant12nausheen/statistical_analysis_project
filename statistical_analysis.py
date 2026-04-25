import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# STEP 1: CREATE SAMPLE DATA (Two regions A and B)
# ============================================================
np.random.seed(42)

# Region A: slightly right-skewed sales data
region_A = np.random.gamma(shape=3, scale=15, size=200) + 10

# Region B: more spread out, slight left skew
region_B = np.random.normal(loc=75, scale=20, size=200)
region_B = np.clip(region_B, 10, 150)

# Add some outliers
region_A = np.append(region_A, [180, 190, 195])
region_B = np.append(region_B, [5, 3, 200, 210])

data = pd.DataFrame({
    'Sales': np.concatenate([region_A, region_B]),
    'Region': ['A'] * len(region_A) + ['B'] * len(region_B)
})

print("=" * 60)
print("DATASET SUMMARY")
print("=" * 60)
print(f"Total records: {len(data)}")
print(f"\nRegion A - Basic Stats:")
print(f"  Mean:    {region_A.mean():.2f}")
print(f"  Median:  {np.median(region_A):.2f}")
print(f"  Std Dev: {region_A.std():.2f}")
print(f"  Skewness:{stats.skew(region_A):.3f}")

print(f"\nRegion B - Basic Stats:")
print(f"  Mean:    {region_B.mean():.2f}")
print(f"  Median:  {np.median(region_B):.2f}")
print(f"  Std Dev: {region_B.std():.2f}")
print(f"  Skewness:{stats.skew(region_B):.3f}")

# ============================================================
# STEP 2: DETECT OUTLIERS using IQR method
# ============================================================
def detect_outliers_iqr(data_arr, label):
    Q1 = np.percentile(data_arr, 25)
    Q3 = np.percentile(data_arr, 75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = data_arr[(data_arr < lower) | (data_arr > upper)]
    print(f"\nRegion {label} Outliers (IQR method):")
    print(f"  IQR bounds: [{lower:.2f}, {upper:.2f}]")
    print(f"  Outlier count: {len(outliers)}")
    print(f"  Outlier values: {sorted(outliers.round(1))}")
    return lower, upper

print("\n" + "=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)
lb_A, ub_A = detect_outliers_iqr(region_A, 'A')
lb_B, ub_B = detect_outliers_iqr(region_B, 'B')

# ============================================================
# STEP 3: CREATE ALL PLOTS IN ONE FIGURE
# ============================================================
fig = plt.figure(figsize=(18, 14))
fig.patch.set_facecolor('#F8F9FA')

gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.3)

colors = {'A': '#4A90D9', 'B': '#E87040'}

# --- Plot 1: Histogram - Region A ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(region_A, bins=25, color=colors['A'], alpha=0.75, edgecolor='white', linewidth=0.5)
ax1.axvline(region_A.mean(), color='navy', linestyle='--', linewidth=2, label=f'Mean={region_A.mean():.1f}')
ax1.axvline(np.median(region_A), color='red', linestyle=':', linewidth=2, label=f'Median={np.median(region_A):.1f}')
ax1.set_title('Histogram — Region A', fontsize=13, fontweight='bold', pad=10)
ax1.set_xlabel('Sales Value')
ax1.set_ylabel('Frequency')
ax1.legend(fontsize=9)
ax1.set_facecolor('#FFFFFF')
ax1.grid(axis='y', alpha=0.3)

# --- Plot 2: Histogram - Region B ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.hist(region_B, bins=25, color=colors['B'], alpha=0.75, edgecolor='white', linewidth=0.5)
ax2.axvline(region_B.mean(), color='darkred', linestyle='--', linewidth=2, label=f'Mean={region_B.mean():.1f}')
ax2.axvline(np.median(region_B), color='blue', linestyle=':', linewidth=2, label=f'Median={np.median(region_B):.1f}')
ax2.set_title('Histogram — Region B', fontsize=13, fontweight='bold', pad=10)
ax2.set_xlabel('Sales Value')
ax2.set_ylabel('Frequency')
ax2.legend(fontsize=9)
ax2.set_facecolor('#FFFFFF')
ax2.grid(axis='y', alpha=0.3)

# --- Plot 3: KDE Comparison ---
ax3 = fig.add_subplot(gs[1, 0])
x_range = np.linspace(0, 220, 400)
kde_A = stats.gaussian_kde(region_A)
kde_B = stats.gaussian_kde(region_B)
ax3.plot(x_range, kde_A(x_range), color=colors['A'], linewidth=2.5, label='Region A')
ax3.fill_between(x_range, kde_A(x_range), alpha=0.15, color=colors['A'])
ax3.plot(x_range, kde_B(x_range), color=colors['B'], linewidth=2.5, label='Region B')
ax3.fill_between(x_range, kde_B(x_range), alpha=0.15, color=colors['B'])
ax3.set_title('KDE — Distribution Comparison', fontsize=13, fontweight='bold', pad=10)
ax3.set_xlabel('Sales Value')
ax3.set_ylabel('Density')
ax3.legend(fontsize=10)
ax3.set_facecolor('#FFFFFF')
ax3.grid(alpha=0.3)

# --- Plot 4: Boxplot Comparison ---
ax4 = fig.add_subplot(gs[1, 1])
bp = ax4.boxplot([region_A, region_B],
                  patch_artist=True,
                  labels=['Region A', 'Region B'],
                  widths=0.5,
                  medianprops=dict(color='black', linewidth=2),
                  flierprops=dict(marker='o', markersize=5, alpha=0.6))
bp['boxes'][0].set_facecolor(colors['A'])
bp['boxes'][0].set_alpha(0.7)
bp['boxes'][1].set_facecolor(colors['B'])
bp['boxes'][1].set_alpha(0.7)
for whisker in bp['whiskers']:
    whisker.set(linewidth=1.5, linestyle='--')
ax4.set_title('Boxplot — Outlier Detection', fontsize=13, fontweight='bold', pad=10)
ax4.set_ylabel('Sales Value')
ax4.set_facecolor('#FFFFFF')
ax4.grid(axis='y', alpha=0.3)
ax4.text(0.98, 0.97, 'Circles = Outliers', transform=ax4.transAxes,
         ha='right', va='top', fontsize=9, color='gray')

# --- Plot 5: Overlaid Histogram ---
ax5 = fig.add_subplot(gs[2, :])
ax5.hist(region_A, bins=30, alpha=0.55, color=colors['A'], label='Region A', edgecolor='white')
ax5.hist(region_B, bins=30, alpha=0.55, color=colors['B'], label='Region B', edgecolor='white')
ax5.axvline(region_A.mean(), color=colors['A'], linestyle='--', linewidth=2,
            label=f'Region A Mean = {region_A.mean():.1f}')
ax5.axvline(region_B.mean(), color=colors['B'], linestyle='--', linewidth=2,
            label=f'Region B Mean = {region_B.mean():.1f}')
ax5.set_title('Overlaid Histogram — Region A vs Region B', fontsize=13, fontweight='bold', pad=10)
ax5.set_xlabel('Sales Value')
ax5.set_ylabel('Frequency')
ax5.legend(fontsize=10)
ax5.set_facecolor('#FFFFFF')
ax5.grid(alpha=0.3)

# Main Title
fig.suptitle('Statistical Distribution Analysis\nRegion A vs Region B',
             fontsize=16, fontweight='bold', y=0.98)

plt.savefig('statistical_plots.png', dpi=150, bbox_inches='tight', facecolor='#F8F9FA')
plt.show()
plt.close()
print("\n[SAVED] statistical_plots.png")

# ============================================================
# STEP 4: PRINT INTERPRETATION PARAGRAPH
# ============================================================
skew_A = stats.skew(region_A)
skew_B = stats.skew(region_B)

interpretation = f"""
{"="*60}
INTERPRETATION
{"="*60}
Region A (mean={region_A.mean():.1f}, median={np.median(region_A):.1f}, std={region_A.std():.1f}):
The distribution is right-skewed (skewness={skew_A:.2f}), meaning most sales
values cluster in the lower range with a long tail toward higher values.
The mean exceeds the median, confirming the right skew. {len(region_A[(region_A < lb_A) | (region_A > ub_A)])} outliers
were detected above the upper IQR bound, representing extreme sales events.

Region B (mean={region_B.mean():.1f}, median={np.median(region_B):.1f}, std={region_B.std():.1f}):
Region B shows a more symmetric, near-normal distribution (skewness={skew_B:.2f})
with a higher mean and wider spread (larger std dev). The spread indicates
greater variability in sales outcomes. {len(region_B[(region_B < lb_B) | (region_B > ub_B)])} outliers were detected,
including both very low and very high values.

CONCLUSION: Region B has higher average sales but more variability/risk.
Region A has more consistent but lower sales. Both show some extreme
outliers that may warrant investigation.
"""
print(interpretation)

# Save interpretation to text file
with open('/home/claude/statistical_analysis_project/interpretation.txt', 'w') as f:
    f.write(interpretation)
print("[SAVED] interpretation.txt")
