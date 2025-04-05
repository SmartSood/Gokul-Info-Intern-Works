const nodemailer = require('nodemailer');
const config = require('./config');

async function sendTestEmail() {
  // Create a transporter object using the SMTP configuration
  let transporter = nodemailer.createTransport({
    host: config.smtpHost,
    port: config.smtpPort,
    secure: config.smtpSecure,
    auth: {
      user: config.smtpUser,
      pass: config.smtpPwd
    }
  });

  // Define email options
  let mailOptions = {
    from: config.supportEmail, // sender address
    to: 'smarthsood@gmail.com', // list of receivers
    subject: 'Hello', // Subject line
    text: 'Hello world?', // plain text body
    html: '<b>Hello world?</b>' // html body
  };

  // Send email
  try {
    let info = await transporter.sendMail(mailOptions);
    console.log('Message sent: %s', info.messageId);
  } catch (error) {
    console.error('Error occurred while sending email:', error);
  }
}

sendTestEmail();
