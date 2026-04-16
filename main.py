import pandas as pd
import matplotlib.pyplot as plt
import os
import random
from datetime import datetime, timedelta

DATA_FILE = "workout_log.csv"

def generate_raw_data():
    print("⚙️ Generating 8 months of raw workout data...")
    records = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=240) # Roughly 8 months

    exercises = ["Dumbbell Pumps", "Push-ups", "Skipping"]
    
    current_date = start_date
    while current_date <= end_date:
        if random.random() > 0.2: 
            for ex in exercises:
                if ex == "Skipping":
                    reps = random.randint(500, 1500)
                else:
                    reps = random.randint(50, 200)
                
                records.append({
                    "Date": current_date.strftime("%Y-%m-%d"),
                    "Exercise": ex,
                    "Reps": reps
                })
        current_date += timedelta(days=1)

    df = pd.DataFrame(records)
    df.to_csv(DATA_FILE, index=False)
    print("✅ Raw data generated successfully!\n")

def analyze_and_plot():
    print("📊 Loading data into Pandas Engine...")
    
    df = pd.read_csv(DATA_FILE)
    
    df['Date'] = pd.to_datetime(df['Date'])
    
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_data = df.groupby(['Month', 'Exercise'])['Reps'].sum().unstack()

    print("\n📈 Processed Monthly Summary:")
    print(monthly_data)
    
    print("\n🎨 Rendering visual dashboard...")
    
    plt.style.use('dark_background')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_data.plot(kind='line', marker='o', ax=ax, linewidth=2, colormap='Set2')

    ax.set_title("8-Month High-Intensity Routine Volume", fontsize=16, fontweight='bold', pad=15)
    ax.set_xlabel("Month", fontsize=12)
    ax.set_ylabel("Total Monthly Reps", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend(title="Exercise Type", fontsize=10)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        generate_raw_data()
    
    analyze_and_plot()