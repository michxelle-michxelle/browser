
root = Tk() 
root.title("WebBrowsers") 
root.geometry("660x660") 

webbrowser.open("www.instagram.com") 
WebDriver driver = new ChromeDriver("C://browser.exe");
webBrowser.get('http://d.com')

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
