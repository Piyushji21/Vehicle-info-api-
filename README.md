# Vehicle-info-api-
This can fetch vehicle details 
Vehicle Info API 🌐🚗

A powerful and fast Vehicle Information API that provides instant details about any vehicle using its registration number.

🚀 Features

· Instant Results - Get vehicle information in milliseconds
· Accurate Data - Reliable and up-to-date vehicle information
· Easy Integration - Simple REST API endpoint
· Secure - Built with security best practices
· 24/7 Availability - Always online and responsive

📋 API Usage

Endpoint

```
GET https://vehicle-info.itxkaal.workers.dev/?num=VEHICLE_NUMBER
```

Example Request

```javascript
fetch('https://vehicle-info.itxkaal.workers.dev/?num=MH02FZ0555')
  .then(response => response.json())
  .then(data => console.log(data));
```

Example Response

```json
{
  "status": "success",
  "vehicle_no": "MH02FZ0555",
  "owner": "SHAH RUKH KHAN",
  "model": "ROLLS-ROYCE MOTOR CARS",
  "maker_model": "BLACK BADGE CULLINAN",
  "vehicle_class": "Motor Car(LMV)",
  "fuel_type": "PETROL",
  "insurance_company": "ICICI LOMBARD",
  "insurance_upto": "16-Mar-2026",
  "address": "MUMBAI (WEST), Maharashtra"
}
```

🛠️ Installation & Setup

Using JavaScript

```javascript
const getVehicleInfo = async (vehicleNumber) => {
  const response = await fetch(`https://vehicle-info.itxkaal.workers.dev/?num=${vehicleNumber}`);
  return await response.json();
};
```

Using cURL

```bash
curl "https://vehicle-info.itxkaal.workers.dev/?num=MH02FZ0555"
```

📊 Response Fields

Field Description
vehicle_no Vehicle registration number
owner Vehicle owner name
model Vehicle model
fuel_type Petrol/Diesel/CNG etc.
insurance_company Insurance provider
insurance_upto Insurance expiry date
address Registered address
And 20+ more fields...

🌐 Live Demo

Check out the live website: Vehicle Info Checker

👨‍💻 Developer

Piyush XD

· Telegram: @thethestar

📄 License

This project is licensed under the MIT License.

---

⭐ Star this repo if you find it useful! ⭐

Built with ❤️ using Cloudflare Workers
