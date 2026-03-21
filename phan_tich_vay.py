import csv

#Tạo hàm tính toán tiền lãi, số tiền phải trả
def tinh_toan(so_tien_vay, lai_suat, so_thang):
    tien_lai_hang_thang = so_tien_vay * lai_suat / 12
    tong_tien_lai = tien_lai_hang_thang * so_thang
    tong_phai_tra = so_tien_vay + tong_tien_lai
    return tong_tien_lai, tong_phai_tra

#Tạo hàm ghi dữ liệu vào file
def xu_ly_ho_so(ten_file_doc, ten_file_ghi):
    ket_qua = []

    try:
        with open(ten_file_doc, "r", encoding="utf-8") as f:
            doc = csv.DictReader(f)
            for dong in doc:
                ten      = dong["ten"]
                so_tien  = float(dong["so_tien_vay"])
                lai_suat = float(dong["lai_suat"])
                so_thang = int(dong["so_thang"])
                tien_lai, tong_tra = tinh_toan(so_tien, lai_suat, so_thang)
                ket_qua.append({
                    "ten": ten,
                    "so_tien_vay": so_tien,
                    "tong_tien_lai": tien_lai,
                    "tong_phai_tra": tong_tra
                })
    except FileNotFoundError:
        print("Không tìm thấy file:", ten_file_doc)
        return
    except KeyError as e:
        print("Không tìm thấy cột:", e)
        return
    else:
        print(f"Đọc xong {len(ket_qua)} khách hàng")

    with open(ten_file_ghi, "w", newline="", encoding="utf-8") as f:
        cot = ["ten", "so_tien_vay", "tong_tien_lai", "tong_phai_tra"]
        writer = csv.DictWriter(f, fieldnames=cot)
        writer.writeheader()
        writer.writerows(ket_qua)
        print(f"Đã ghi kết quả ra file: {ten_file_ghi}")

xu_ly_ho_so("khach_hang_vay.csv", "ket_qua_vay.csv")
