import requests

url_rates = "https://open.er-api.com/v6/latest/USD"
url_weather = "https://wttr.in/Ho_Chi_Minh_City"

try:
    r_rates = requests.get(url_rates)
    d_rates = r_rates.json()
except Exception as e:
    print(f"Lỗi kết nối đến API tỷ giá: {e}")

try:
    params = {"format": "j1"}
    r_weather = requests.get(url_weather, params = params)
    d_weather = r_weather.json()
except Exception as e:
    print(f"Lỗi kết nối đến API thời tiết: {e}")
  


print("===== BÁO CÁO BUỔI SÁNG =====")
print(f"📅 Thời gian cập nhật: {d_rates["time_last_update_utc"]}")
print(f"💱 Tỷ giá USD/VND: {round(d_rates['rates']['VND']):,}")
print(f"🌡️ Nhiệt độ TP.HCM: {d_weather["current_condition"][0]["temp_C"]}")
print("==============================")
