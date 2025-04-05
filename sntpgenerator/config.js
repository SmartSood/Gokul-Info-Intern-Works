require('dotenv').config();

module.exports = {
  supportEmail: process.env.SUPPORT_EMAIL,
  smtpHost: process.env.SMTP_HOST,
  smtpPort: process.env.SMT_PORT,
  smtpSecure: process.env.SMTP_SECURE === 'true', // Converts string to boolean
  smtpUser: process.env.SMTP_USER,
  smtpPwd: process.env.SMTP_PWD
};
