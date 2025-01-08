app.config['smart_Card'] = 'C:\\WINDOWS\system32\DRIVERS\umpass.sys', "C:\Users\usogv\OneDrive\Desktop\smartcard_cert.txt", "C:\Users\usogv\OneDrive\Desktop\tagliov70pc.txt", ;
app.config['Taglio_Certificates'] = "C:\Users\usogv\Downloads\pkadmin (1)\pkadmin\CA Root Certificates\pivkeydeviceca.crl", "C:\Users\usogv\Downloads\pkadmin (1)\pkadmin\CA Root Certificates\pivkeydeviceca.crt", "C:\Users\usogv\Downloads\pkadmin (1)\pkadmin\CA Root Certificates\server-ca.crt", "C:\Users\usogv\Downloads\pkadmin (1)\pkadmin\CA Root Certificates\tagliorootca.crl", "C:\Users\usogv\Downloads\pkadmin (1)\pkadmin\CA Root Certificates\tagliorootca.crt", '', 
app.config['Smart_Card_Reader'] ='', 
 'C:\WINDOWS\System32\DRIVERS\scfilter.sys',
 'C:\WINDOWS\system32\DRIVERS\UMDF\WUDFUsbccidDriver.dll',
 'C:\WINDOWS\system32\DRIVERS\winusb.sys',
 'C:\WINDOWS\system32\drivers\WUDFRd.sys',

app.config['USB_Serial_Controllers'] = 

'C:\WINDOWS\system32\DRIVERS\UMDF\UsbXhciCompanion.dll',
'C:\WINDOWS\system32\DRIVERS\USBXHCI.SYS ' ,
'C:\WINDOWS\system32\DRIVERS\usbccgp.sys ' ,
'C:\WINDOWS\system32\DRIVERS\USBHUB3.SYS ',
'usb4deviceroute.inf_amd64_20da523aab577a9c\Usb4DeviceRouter.sys',
'usb4hostrouter.inf_amd_d1f4f1b9ed26b447\Usb4HostRouter.sys'

app.config['Microsoft_Input_Configuration'] = 'C:\WINDOWS\system32\DRIVERS\MTConfig.sys'

app.config['USB_Input_Device'] = 'C:\WINDOWS\system32\DRIVERS\hidclass.sys',
'C:\WINDOWS\system32\DRIVERS\hidparse.sys',
'C:\WINDOWS\system32\DRIVERS\hidusb.sys',

app.config[USB_Connector_Managers] = 'C:\WINDOWS\system32\DRIVERS\UcmUcsiAcpiClient.sys'









root = Tk() 
root.title("WebBrowsers") 
root.geometry("660x660") 


WebDriver driver = new ChromeDriver("C://browser.exe");
webBrowser.open('www.instagram.com')

 driver.findElement(By.xpath("//*[@id=\"confirmButton\"]")).click(); Thread.sleep(3000);


//DBS PROMPT

    Alert alert = driver.switchTo().alert();  alert.accept();

        driver.findElement(By.id("dbs")).sendKeys("000000);
        driver.findElement(By.className("dbs-button")).click(); Thread.sleep(3000);
    }






///REGISTER



/// LOGIN     
        driver.findElement(By.id("luser")).sendKeys("xyz@gmail.com"); 
        driver.findElement(By.id("password")).sendKeys("xyz12345");
        driver.findElement(By.className("signin-button")).click();
    }
