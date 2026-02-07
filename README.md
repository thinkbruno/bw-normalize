<h1 align="left">Project description</h1>

###

<p align="left">Converter of date values and currency values.<br><br>Adjusts the values to be able to save to the database and also adjusts some output formats for returns.<br><br>To convert a date to the US standard (for database), import NormalizeDates() class from normalize.dates.normalize_dates import NormalizeDates then use NormalizeDates().normalize(string_of_your_date)<br><br>Accepted date formats: 20/03/1990 20-30-1990 March 30th, 1990 20 de marÃ§o de 1990<br><br>To convert the date to a detailed format, import ConvertDates() class from normalize.dates.convert_dates import ConvertDates then use ConvertDates(string_your_format).convert(string_of_your_date*) * US standard - 1990-03-20<br><br>Accepted formats: /br returns 20/03/1990 full_br returns 20 de marÃ§o de 1990 full_us returns March 30th, 1990<br><br>To convert a currency value, import the NormalizeCurrency() class from normalize.currency.currency import NormalizeCurrency<br><br>then use NormalizeCurrency()normalize_currency(string_of_your_currency*) function<br><br>Accepted currency: R$ 5.000,00 R$ 5000,00 R$ 5,000 $ 5,000.00<br><br>then returns 5000.0<br><br>To convert a currency value, import the NormalizeCurrency() class from normalize.currency.currency import NormalizeCurrency<br><br>then use NormalizeCurrency(locale*)convert_currency(float_of_your_currency*) function<br><br>the “locale” argument return according to the given argument:<br>locale=”en_US” returns $ 5,000.00 locale=”pt_BR” returns R$ 5.000,00</p>

###

<h2 align="left">Developed by</h2>

###

<div align="left">
  <a href="https://www.linkedin.com/in/ramosbruno90/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="40" alt="linkedin logo"  />
  </a>
</div>

###

<div align="left">
  <a href="https://www.linkedin.com/in/wellington-alves-rosendo/" target="_blank">
    <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="40" alt="linkedin logo"  />
  </a>
</div>

###
