package com.divyanshi.RestAssuredTest;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import java.util.List;
import java.util.Map;

public class UserApiTest {

    @BeforeClass
    public void setUp() {
        RestAssured.baseURI = "https://fakestoreapi.com";
    }

    @Test
    public void testFirstNamesPresent() {
        Response response = RestAssured.given().log().all().get("/users").then().log().all().extract().response();

        // Print response status code
        int statusCode = response.getStatusCode();
        System.out.println("Response Status Code: " + statusCode);

        // Validate status code
        Assert.assertEquals(statusCode, 200, "Unexpected status code");

        // Print response content type
        String contentType = response.getContentType();
        System.out.println("Response Content Type: " + contentType);

        // Validate content type
        Assert.assertEquals(contentType, "application/json; charset=utf-8", "Unexpected content type");

        // Get firstnames from the response payload
        List<String> firstNames = response.jsonPath().getList("name.firstname");
        if ( firstNames.contains("david")) {
            System.out.println("david users is present in response payload");
        } else {
            System.out.println("Test Case 1 Fail: There is not don name present");
        }

        // Validate presence of specific firstnames
        Assert.assertTrue(firstNames.contains("david"), "David not found");
        if ( firstNames.contains("don")) {
            System.out.println("don users is present in response payload");
        } else {
            System.out.println("Test Case 1 Fail: There is not don name present");
        }
        Assert.assertTrue(firstNames.contains("don"), "Don not found");
        if ( firstNames.contains("miriam")) {
            System.out.println("miriam users is present in response payload");
        } else {
            System.out.println("Test Case 1 Fail: There is not don name present");
        }
        Assert.assertTrue(firstNames.contains("miriam"), "Miriam not found");
    }

    @Test
    public void testLatAndLongNotNull() {
        Response response = RestAssured.given().log().all().get("/users").then().log().all().extract().response();

        // Print response status code
        int statusCode = response.getStatusCode();
        System.out.println("Response Status Code: " + statusCode);

        // Validate status code
        Assert.assertEquals(statusCode, 200, "Unexpected status code");

        // Print response content type
        String contentType = response.getContentType();
        System.out.println("Response Content Type: " + contentType);

        // Validate content type
        Assert.assertEquals(contentType, "application/json; charset=utf-8", "Unexpected content type");

        List<Map<String, String>> geolocationList = response.jsonPath().getList("address.geolocation");

        for (Map<String, String> geolocation : geolocationList) {
            if (geolocation.containsKey("lat")) {
                System.out.println("Lat is not null");
            } else {
                System.out.println("Lat is null");
            }

            Assert.assertNotNull(geolocation.get("lat"), "Lat is null");
            if (geolocation.containsKey("long")) {
                System.out.println("Long is not null");
            } else {
                System.out.println("Long is null");
            }

            Assert.assertNotNull(geolocation.get("long"), "Long is null");
        }
    }

    @Test
    public void testPasswordComplexity() {
        Response response = RestAssured.given().log().all().get("/users").then().log().all().extract().response();

        // Print response status code
        int statusCode = response.getStatusCode();
        System.out.println("Response Status Code: " + statusCode);

        // Validate status code
        Assert.assertEquals(statusCode, 200, "Unexpected status code");

        // Print response content type
        String contentType = response.getContentType();
        System.out.println("Response Content Type: " + contentType);

        // Validate content type
        Assert.assertEquals(contentType, "application/json; charset=utf-8", "Unexpected content type");

        List<String> passwords = response.jsonPath().getList("password");

        for (String password : passwords) {
            // Validate password complexity (at least 1 character, 1 special character, 1 number)
            if (password.matches("^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).+$")) {
                System.out.println("password contains at least 1 character, 1 special character and 1 number in it");
            } else {
                System.out.println("password doesn't contains at least 1 character, 1 special character and 1 number in it");
            }
            Assert.assertTrue(password.matches("^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[@#$%^&+=]).+$"), "Password does not meet complexity requirements");
        }
    }
}
