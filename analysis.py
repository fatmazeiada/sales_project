import pandas as pd
import matplotlib.pyplot as plt


# رفع ملف CSV من جهازك
print("📂 من فضلك اختاري ملف sales_data.csv من جهازك")


# قراءة البيانات
df = pd.read_csv("sales_data.csv")

# إنشاء عمود جديد = إجمالي العملية (Quantity * Price)
df["Total"] = df["Quantity"] * df["Price"]

# إجمالي المبيعات لكل منتج
sales_summary = df.groupby("Product")["Total"].sum().reset_index()

print("📊 إجمالي المبيعات لكل منتج:")
print(sales_summary)

# رسم جرافيك يوضح أكتر المنتجات مبيعًا
plt.figure(figsize=(8,5))
plt.bar(sales_summary["Product"], sales_summary["Total"], color="skyblue")
plt.xlabel("Product")
plt.ylabel("Total Sales ($)")
plt.title("Total Sales per Product")
plt.show()

# استخراج أهم المنتجات
top_products = sales_summary.sort_values(by="Total", ascending=False).head(5)
print("\n🔥 Top 5 منتجات:")
print(top_products)

# الإيرادات الكلية
total_revenue = df["Total"].sum()
print(f"\n💰 إجمالي الإيرادات: ${total_revenue}")
