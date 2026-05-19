# 1. Phân tích
# - I: + Họ tên bệnh nhân str
#   + Mã bệnh án str
#   + Khoa/Phòng khám chỉ định str
# - O: Phiếu khám bệnh điện tử hiển thị trên màn hình.

# 2. Giải pháp
# - Sử dụng `input()` để tiếp nhập thông tin từ bàn phím.
# - Sử dụng `print()` để thiết kế giao diện phiếu khám, 
# truyền các biến đã nhập vào đúng vị trí hiển thị để tránh lỗi logic lệch thông tin.

ten_benh_nhan = input("1. Nhập họ và tên bệnh nhân: ")
ma_benh_an = input("2. Nhập mã bệnh án: ")
khoa_chi_dinh = input("3. Nhập khoa/phòng khám chỉ định: ")

print("----- PHIẾU KHÁM BỆNH ĐIỆN TỬ -----")
print(f"Bệnh nhân: {ten_benh_nhan} - Mã BA: {ma_benh_an} - Chuyển tới: {khoa_chi_dinh} ")
