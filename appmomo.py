from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/payment-notify', methods=['POST'])
def payment_notify():
    data = request.json
    # Xử lý dữ liệu thông báo từ MoMo
    print("Received payment notification:", data)
    
    # Thực hiện các hành động cần thiết, ví dụ: cập nhật trạng thái đơn hàng, gửi email xác nhận, v.v.
    
    # Trả về phản hồi cho MoMo
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)