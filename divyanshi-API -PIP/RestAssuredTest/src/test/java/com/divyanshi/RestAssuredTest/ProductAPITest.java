package com.divyanshi.RestAssuredTest;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import java.util.List;

public class ProductAPITest {

    @BeforeClass
    public void setUp() {
        RestAssured.baseURI = "https://fakestoreapi.com";
    }

    @Test
    public void testGetProducts() {
        Response response = RestAssured.given().log().all().get("/products").then().log().all().extract().response();

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

        // Validate number of products
        List<Object> products = response.jsonPath().getList("");
        if (products.size() == 20) {
            System.out.println("Test Case 1 Pass: 20 products exist");
        } else {
            System.out.println("Test Case 1 Fail: There are not 20 products");
        }
        Assert.assertEquals(products.size(), 20, "Incorrect number of products");
    }



    @Test
    public void testUniqueIds() {
        Response response = RestAssured.given().log().all().get("/products").then().log().all().extract().response();

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

        // Validate unique IDs
        List<Integer> ids = response.jsonPath().getList("id");
        long distinctCount = ids.stream().distinct().count();
        System.out.println("Number of IDs: " + ids.size());
        if (distinctCount == ids.size()) {
            System.out.println("All IDs are unique");
        } else {
            System.out.println("Duplicate IDs found");
        }
        Assert.assertEquals(ids.size(), distinctCount, "Not all IDs are unique");
       // Assert.assertEquals(ids.size(), ids.stream().distinct().count(), "Not all IDs are unique");
    }
}
