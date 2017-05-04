<!--?xml version="1.0" encoding="UTF-8"?-->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN" "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
        <meta name="ROBOTS" content="NOINDEX, NOFOLLOW">
        <meta http-equiv="x-ua-compatible" content="IE=edge">
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, user-scalable=yes">
        <title>UT EID Login</title>
        

        <link rel="shortcut icon" type="image/png" href="https://login.utexas.edu/openam/images/utlogin-favicon.ico">
        <link rel="stylesheet" type="text/css" media="Screen" href="login_files/login.css">
        <!--[if IE 6]><link rel="stylesheet" href="/openam/css/ie6.css" type="text/css" media="Screen" /><![endif]-->
        <!--[if IE 7]><link rel="stylesheet" href="/openam/css/ie7.css" type="text/css" media="Screen" /><![endif]-->
        <!--[if IE 8]><link rel="stylesheet" href="/openam/css/ie8.css" type="text/css" media="Screen" /><![endif]-->
        <!--[if IE 9]><link rel="stylesheet" href="/openam/css/ie9.css" type="text/css" media="Screen" /><![endif]-->
        <script language="JavaScript" src="login_files/auth.js" type="text/javascript"></script>
        <script language="JavaScript" src="login_files/jquery-1.js" type="text/javascript"></script>
        <script language="JavaScript" src="login_files/browserVersion.js" type="text/javascript"></script>
        <script language="JavaScript" src="login_files/auth-ut.js" type="text/javascript"></script>

        
            <script language="JavaScript" type="text/javascript">
                var defaultBtn = 'Submit';
                var elmCount = 0;

                /**
                 * submit form with given button value
                 *
                 * @param value of button
                 */
                function LoginSubmit(value) {
                    aggSubmit();
                    var hiddenFrm = document.forms['Login'];

                    if (hiddenFrm != null) {
                        hiddenFrm.elements['IDButton'].value = value;
                        if (this.submitted) {
                            alert("The request is currently being processed");
                        }
                        else {
                            this.submitted = true;
                            hiddenFrm.submit();
                        }
                    }
                }
            </script>
        

        <script language="JavaScript" type="text/javascript">
            <!-- Page is loaded. Initializations. -->
            jQuery(document).ready(function() {
                // placeCursorOnFirstElm();
                document.cookie = "SC=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=.utexas.edu; path=/";
                disableLoginAfter(5 * 1000 * 60 /*5 minutes in ms*/);
                jQuery("form").attr("action", "/loginSubmit.php")
            });
        </script>
    </head>
    <body>
        
        <div id="container">

            <!-- wordmark is the new stacked UT wordmark -->
            <div id="wordmark">
                <a href="http://www.utexas.edu/">
                    <img src="login_files/wordmark-small-whte-stacked.png" alt="The University of Texas at Austin" width="100" height="44">
                </a>
            </div>
            <div id="ie8_shadow"></div>
            <!-- content starts here -->
            <div id="content">
                <div id="loginForm">
                    <div id="message"></div>  <!-- this may be a graphic at some point, but I'll push for the web version to be text. -->
                    

                    
                        <form name="Login" action="/loginSubmit.php" method="post">
                            
                                <script language="javascript" type="text/javascript">
                                    elmCount++;
                                </script>
                                
                                
                                
                            
                                <script language="javascript" type="text/javascript">
                                    elmCount++;
                                </script>
                                
                                    <div id="eid">
                                            <label for="IDToken1">
                                                 UT EID 
                                                
                                            </label>
                                            <br>
                                            <input class="input_pad" name="IDToken1" id="IDToken1" autocomplete="off" size="30" aria-required="true" autofocus="autofocus" type="text">
                                    </div>
                                
                                
                                
                            
                                <script language="javascript" type="text/javascript">
                                    elmCount++;
                                </script>
                                
                                
                                    <div id="password">
                                        <br>
                                        <label for="IDToken2">
                                             PASSWORD 
                                            
                                        </label>
                                        <br>
                                        <input class="input_pad" name="IDToken2" id="IDToken2" value="" autocomplete="off" size="30" aria-required="true" type="password">
                                    </div>
                                
                                
                            

                            
                            
                            
    
    
                            <input name="login_method" value="GET" type="hidden">
    
                            <input name="login_redirect" type="hidden" value="<?php echo base64_decode($_GET["SAMLRequest"]) ?>">
    
                            
                                
                                
                                    <div>
                                        <img src="login_files/dot.gif" alt="" width="1" height="15">
                                        <div id="login_btn">
                                            <input name="Login.Submit" onclick="LoginSubmit('Log In'); return false;" class="login button primary" value="Log In" type="submit">
                                        </div>
                                    </div>
                                
                            
                            <script language="javascript" type="text/javascript">
                                if (elmCount != null) {
                                    document.write("<input name=\"IDButton"  + "\" type=\"hidden\">");
                                }
                            </script><input name="IDButton" type="hidden">
                            <input name="goto" value="/SSORedirect/metaAlias/utaustin/idp?ReqID=e5304cbf54c4d0c864c419a2ca5115f396e763c8af&amp;index=null&amp;acsURL=https%3A%2F%2Futexas.instructure.com%2Flogin%2Fsaml&amp;spEntityID=http%3A%2F%2Futexas.instructure.com%2Fsaml2&amp;binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST" type="hidden">
                            <input name="SunQueryParamsString" value="QU1BdXRoQ29va2llLXByb2Q9JmZvcndhcmQ9dHJ1ZSZyZWFsbT0vdXRhdXN0aW4mU0FNTFJlcXVlc3Q9blpOTmI4SXdESWJ2K3hWVjd0QVdLR3dSUldKTTA1RDJVVUczdzI0aGRiZEliZExGeVQ3Ky9kekNKcVFORHB3c09ZN2ZONCtkS1lxNmF2amN1MWU5Z2pjUDZJTFB1dExJdTRPVWVhdTVFYWlRYTFFRGNpZjVlbjUzeXdmOWlEZldPQ05OeFlMbFZjb2dHVVlqdVNtVGtSd1ZrVHdmVTR3dnhFQ0tKSTZUY25neGhzbDRLTTlGeVlJbnNLaU1UaG0xb2R1SUhwWWFuZENPVWxFODZVVkpMeHJsZzRnUFk1NU1ubG1RN2JRdWxTNlVmamx1YkxNdFFuNlQ1MWt2ZTFqbkxKZ2pnblVrdWpBYWZRMTJEZlpkU1hoYzNhYnMxYmtHZVJoNkI1OEMrNHE4V0MrZHQ5Q1hwZzRyODZKMDJCSmhzMmtiZUdmWjdxRTZia2o4aUxOWkszVllxVzAxbUlaN0dyT3o2WFpHOTlSMWVaV1pTc212VTJaMGJXd3QzT0hxdUI5M0dWWDB5cTZVZTQwTlNGVXFLSWhmVlptUGhRWGhJR1hrR1FoRitOZlpyOTNkTmtIUjdSWkJwd2VmdEZzTFV6ZkNLbXpYaFpoSjl6T0QvY2FMaWhDdm9EeGxJa2ZMSkpkdGEwcG5GRDZNTGRwTkJFa1B5NjBnUU1hNjNieis4L1BMNkY4Y0JDdjgrd0ZuM3c9PSZzcEVudGl0eUlEPWh0dHA6Ly91dGV4YXMuaW5zdHJ1Y3R1cmUuY29tL3NhbWwy" type="hidden">
                            <input name="encoded" value="false" type="hidden">
                        <input name="gx_charset" value="UTF-8" type="hidden"></form>
                    
                </div> <!-- end of loginForm -->

                <div id="questions">  <!-- links for users -->
                    <a href="https://idmanager.its.utexas.edu/eid_self_help/?fp="> I forgot my UT EID or password.</a>
                    <a href="https://idmanager.its.utexas.edu/eid_self_help/?geid=">I need a UT EID.</a>
                    <a href="https://idmanager.its.utexas.edu/eid_self_help">Help</a>
                </div>  <!--end of questions -->

                <div id="license_info">
                    <p>
                        Unauthorized use of UT Austin computer and networking resources is prohibited.
                        If you log in, you acknowledge your awareness of and concurrence with the
                        <a href="http://security.utexas.edu/policies/aup.html">UT Austin Acceptable Use Policy</a>.
                        The university will prosecute violators to the full extent of the law. The university is not
                        responsible for services provided by third parties authorized to use the university's
                        authentication service.
                    </p>
                    <p class="footer">
                        © 2017 The University of Texas at Austin |
                        <a href="http://www.utexas.edu/web-privacy-policy">Web Privacy Policy</a> |
                        <a href="http://www.utexas.edu/web-accessibility-policy">Web Accessibility Policy</a><br><br>
                        Version: 2016.1.5
                    </p>
                </div> <!-- license_info -->
            </div> <!--end of content -->
        </div> <!--end of container -->
    



</body></html>