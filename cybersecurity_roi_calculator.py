# Cybersecurity ROI Calculator for Renewable Energy Utilities
# Enhanced version with industry-specific metrics and visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Set up plotting style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class CybersecurityROICalculator:
    """
    Enhanced cybersecurity ROI calculator with industry-specific considerations
    for renewable energy utilities.
    """
    
    def __init__(self):
        # Industry benchmarks for renewable energy sector
        self.industry_benchmarks = {
            'avg_breach_cost_energy': 6_450_000,  # IBM Cost of Data Breach 2024 - Energy sector
            'baseline_breach_probability': 0.023,  # 2.3% monthly probability
            'operational_downtime_cost_per_hour': 50_000,  # Utility-specific
            'regulatory_fine_multiplier': 1.5,
            'reputation_damage_multiplier': 0.3
        }
    
    def calculate_baseline_risk(self, attack_surface_size, asset_criticality_score=1.0):
        """
        Calculate baseline cyber risk without zero trust implementation.
        
        Parameters:
        - attack_surface_size: Number of critical assets/endpoints
        - asset_criticality_score: Multiplier for high-value assets (1.0-3.0)
        """
        baseline_probability = (
            self.industry_benchmarks['baseline_breach_probability'] * 
            (attack_surface_size / 1000) *  # Normalize by typical org size
            asset_criticality_score
        )
        return min(baseline_probability, 0.95)  # Cap at 95% probability
    
    def calculate_breaches_prevented(self, attack_surface_size, zero_trust_effectiveness, 
                                   time_period_months=1, asset_criticality_score=1.0):
        """
        Enhanced calculation of breaches prevented with confidence intervals.
        """
        baseline_risk = self.calculate_baseline_risk(attack_surface_size, asset_criticality_score)
        
        # Calculate expected breaches prevented
        breaches_prevented = baseline_risk * zero_trust_effectiveness * time_period_months
        
        # Calculate confidence intervals (Monte Carlo approach)
        np.random.seed(42)
        simulations = 1000
        results = []
        
        for _ in range(simulations):
            # Add uncertainty to parameters
            risk_variation = np.random.normal(baseline_risk, baseline_risk * 0.2)
            effectiveness_variation = np.random.normal(zero_trust_effectiveness, zero_trust_effectiveness * 0.1)
            
            risk_variation = max(0, min(risk_variation, 1))
            effectiveness_variation = max(0, min(effectiveness_variation, 1))
            
            sim_result = risk_variation * effectiveness_variation * time_period_months
            results.append(sim_result)
        
        confidence_intervals = {
            'low': np.percentile(results, 10),
            'high': np.percentile(results, 90),
            'median': np.median(results)
        }
        
        return breaches_prevented, confidence_intervals
    
    def calculate_comprehensive_savings(self, breaches_prevented, custom_breach_cost=None,
                                      include_downtime=True, avg_downtime_hours=24):
        """
        Calculate comprehensive financial impact including multiple cost categories.
        """
        breach_cost = custom_breach_cost or self.industry_benchmarks['avg_breach_cost_energy']
        
        # Direct breach costs
        direct_savings = breaches_prevented * breach_cost
        
        # Operational downtime costs (critical for utilities)
        downtime_savings = 0
        if include_downtime:
            downtime_cost_per_breach = (
                self.industry_benchmarks['operational_downtime_cost_per_hour'] * 
                avg_downtime_hours
            )
            downtime_savings = breaches_prevented * downtime_cost_per_breach
        
        # Regulatory compliance savings
        regulatory_savings = direct_savings * self.industry_benchmarks['regulatory_fine_multiplier'] * 0.1
        
        # Reputation/customer trust savings
        reputation_savings = direct_savings * self.industry_benchmarks['reputation_damage_multiplier']
        
        return {
            'direct_breach_costs': direct_savings,
            'operational_downtime': downtime_savings,
            'regulatory_compliance': regulatory_savings,
            'reputation_protection': reputation_savings,
            'total_savings': direct_savings + downtime_savings + regulatory_savings + reputation_savings
        }
    
    def generate_monthly_report(self, attack_surface_size, zero_trust_effectiveness, 
                               custom_breach_cost=None, asset_criticality_score=1.0):
        """
        Generate comprehensive monthly cybersecurity ROI report.
        """
        # Calculate breaches prevented
        breaches_prevented, confidence_intervals = self.calculate_breaches_prevented(
            attack_surface_size, zero_trust_effectiveness, 1, asset_criticality_score
        )
        
        # Calculate savings breakdown
        savings_breakdown = self.calculate_comprehensive_savings(
            breaches_prevented, custom_breach_cost
        )
        
        # Calculate confidence interval savings
        savings_low = self.calculate_comprehensive_savings(
            confidence_intervals['low'], custom_breach_cost
        )['total_savings']
        
        savings_high = self.calculate_comprehensive_savings(
            confidence_intervals['high'], custom_breach_cost
        )['total_savings']
        
        return {
            'breaches_prevented': breaches_prevented,
            'confidence_intervals': confidence_intervals,
            'savings_breakdown': savings_breakdown,
            'savings_confidence_range': (savings_low, savings_high),
            'roi_metrics': self._calculate_roi_metrics(savings_breakdown, attack_surface_size)
        }
    
    def _calculate_roi_metrics(self, savings_breakdown, attack_surface_size):
        """Calculate additional ROI metrics for executive reporting."""
        # Estimate zero trust implementation cost (rough approximation)
        estimated_zt_monthly_cost = attack_surface_size * 25  # $25 per endpoint/month
        
        roi_ratio = savings_breakdown['total_savings'] / estimated_zt_monthly_cost
        
        return {
            'estimated_monthly_investment': estimated_zt_monthly_cost,
            'roi_ratio': roi_ratio,
            'cost_per_dollar_saved': estimated_zt_monthly_cost / max(savings_breakdown['total_savings'], 1)
        }

# Initialize calculator
calculator = CybersecurityROICalculator()

# Example usage with realistic parameters for a renewable energy utility
print("=== CYBERSECURITY ROI CALCULATOR FOR RENEWABLE ENERGY UTILITIES ===\n")
print("This calculator provides executive-ready metrics for board presentations.\n")

# Example parameters (you can modify these)
ATTACK_SURFACE_SIZE = 2500  # Number of critical endpoints/systems
ZERO_TRUST_EFFECTIVENESS = 0.75  # 75% risk reduction
CUSTOM_BREACH_COST = 8_000_000  # Custom cost estimate
ASSET_CRITICALITY = 2.0  # High criticality for utility infrastructure

# Generate report
monthly_report = calculator.generate_monthly_report(
    attack_surface_size=ATTACK_SURFACE_SIZE,
    zero_trust_effectiveness=ZERO_TRUST_EFFECTIVENESS,
    custom_breach_cost=CUSTOM_BREACH_COST,
    asset_criticality_score=ASSET_CRITICALITY
)

# Display results
print("📊 EXECUTIVE SUMMARY - MONTHLY CYBERSECURITY ROI")
print("=" * 60)
print(f"Estimated breaches prevented this month: {monthly_report['breaches_prevented']:.3f}")
print(f"Confidence range: {monthly_report['confidence_intervals']['low']:.3f} - {monthly_report['confidence_intervals']['high']:.3f}")
print()

print("💰 FINANCIAL IMPACT BREAKDOWN")
print("-" * 40)
savings = monthly_report['savings_breakdown']
for category, amount in savings.items():
    if category != 'total_savings':
        print(f"{category.replace('_', ' ').title()}: ${amount:,.0f}")
print(f"\n🎯 TOTAL ESTIMATED SAVINGS: ${savings['total_savings']:,.0f}")
print(f"Savings range: ${monthly_report['savings_confidence_range'][0]:,.0f} - ${monthly_report['savings_confidence_range'][1]:,.0f}")

print("\n📈 ROI METRICS")
print("-" * 40)
roi = monthly_report['roi_metrics']
print(f"Estimated monthly ZT investment: ${roi['estimated_monthly_investment']:,.0f}")
print(f"ROI ratio: {roi['roi_ratio']:.1f}x return on investment")
print(f"Cost efficiency: ${roi['cost_per_dollar_saved']:.2f} spent per dollar saved")

# Create visualizations for executive presentation
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Cybersecurity ROI Dashboard - Monthly Report', fontsize=16, fontweight='bold')

# 1. Savings breakdown pie chart
savings_data = {k: v for k, v in savings.items() if k != 'total_savings' and v > 0}
ax1.pie(savings_data.values(), labels=[k.replace('_', ' ').title() for k in savings_data.keys()], 
        autopct='%1.1f%%', startangle=90)
ax1.set_title('Savings Breakdown by Category')

# 2. Confidence interval visualization
categories = ['Low Estimate', 'Expected', 'High Estimate']
values = [monthly_report['confidence_intervals']['low'], 
          monthly_report['breaches_prevented'],
          monthly_report['confidence_intervals']['high']]
bars = ax2.bar(categories, values, color=['lightcoral', 'steelblue', 'lightgreen'])
ax2.set_title('Breaches Prevented (with Confidence Intervals)')
ax2.set_ylabel('Number of Breaches')
for bar, value in zip(bars, values):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001, 
             f'{value:.3f}', ha='center', va='bottom')

# 3. Monthly trend simulation (example data)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
cumulative_savings = np.cumsum([savings['total_savings']] * 6)
ax3.plot(months, cumulative_savings, marker='o', linewidth=3, markersize=8)
ax3.set_title('Cumulative Savings Projection')
ax3.set_ylabel('Cumulative Savings ($)')
ax3.grid(True, alpha=0.3)
for i, value in enumerate(cumulative_savings):
    ax3.text(i, value + cumulative_savings[-1]*0.02, f'${value/1e6:.1f}M', 
             ha='center', va='bottom', fontsize=9)

# 4. ROI comparison
investment_cost = roi['estimated_monthly_investment']
total_savings = savings['total_savings']
ax4.bar(['Investment', 'Savings'], [investment_cost, total_savings], 
        color=['orange', 'green'], alpha=0.7)
ax4.set_title('Monthly Investment vs. Savings')
ax4.set_ylabel('Amount ($)')
for i, (label, value) in enumerate([('Investment', investment_cost), ('Savings', total_savings)]):
    ax4.text(i, value + max(investment_cost, total_savings)*0.02, 
             f'${value:,.0f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# Generate executive summary table
summary_df = pd.DataFrame({
    'Metric': [
        'Breaches Prevented (Monthly)',
        'Total Financial Impact',
        'Direct Breach Cost Savings',
        'Operational Downtime Savings',
        'Regulatory Compliance Savings',
        'Reputation Protection Value',
        'Zero Trust Monthly Investment',
        'Return on Investment Ratio',
        'Cost Per Dollar Saved'
    ],
    'Value': [
        f"{monthly_report['breaches_prevented']:.3f}",
        f"${savings['total_savings']:,.0f}",
        f"${savings['direct_breach_costs']:,.0f}",
        f"${savings['operational_downtime']:,.0f}",
        f"${savings['regulatory_compliance']:,.0f}",
        f"${savings['reputation_protection']:,.0f}",
        f"${roi['estimated_monthly_investment']:,.0f}",
        f"{roi['roi_ratio']:.1f}x",
        f"${roi['cost_per_dollar_saved']:.2f}"
    ]
})

print("\n📋 EXECUTIVE SUMMARY TABLE")
print("=" * 50)
print(summary_df.to_string(index=False))

# Interactive parameter adjustment function
def calculate_scenario(attack_surface, zt_effectiveness, breach_cost=None, criticality=1.0):
    """Quick scenario calculation for what-if analysis."""
    report = calculator.generate_monthly_report(
        attack_surface, zt_effectiveness, breach_cost, criticality
    )
    
    print(f"\n🔍 SCENARIO ANALYSIS")
    print(f"Attack Surface: {attack_surface:,} endpoints")
    print(f"ZT Effectiveness: {zt_effectiveness:.1%}")
    print(f"Asset Criticality: {criticality:.1f}x")
    print(f"Breaches Prevented: {report['breaches_prevented']:.3f}")
    print(f"Total Savings: ${report['savings_breakdown']['total_savings']:,.0f}")
    print(f"ROI Ratio: {report['roi_metrics']['roi_ratio']:.1f}x")
    
    return report

# Example scenarios for sensitivity analysis
print("\n\n🎯 SCENARIO ANALYSIS")
print("=" * 60)

scenarios = [
    ("Conservative", 1500, 0.60, None, 1.0),
    ("Current Baseline", 2500, 0.75, None, 2.0),
    ("Optimistic", 3500, 0.85, None, 2.5)
]

scenario_results = []
for name, surface, effectiveness, cost, criticality in scenarios:
    print(f"\n--- {name} Scenario ---")
    result = calculate_scenario(surface, effectiveness, cost, criticality)
    scenario_results.append((name, result))

print("\n\n📊 READY FOR EXECUTIVE PRESENTATION")
print("=" * 50)
print("This analysis provides:")
print("✅ Quantified breach prevention metrics")
print("✅ Comprehensive financial impact assessment")
print("✅ Confidence intervals for risk management")
print("✅ Industry-specific cost considerations")
print("✅ Visual dashboard for board presentations")
print("✅ Scenario analysis for strategic planning")
