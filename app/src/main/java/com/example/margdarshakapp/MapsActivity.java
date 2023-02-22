package com.example.margdarshakapp;

import androidx.fragment.app.FragmentActivity;

import android.os.Bundle;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.OnMapReadyCallback;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.example.margdarshakapp.databinding.ActivityMapsBinding;

public class MapsActivity extends FragmentActivity implements OnMapReadyCallback {

    private GoogleMap mMap;
    private ActivityMapsBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMapsBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // Obtain the SupportMapFragment and get notified when the map is ready to be used.
        SupportMapFragment mapFragment = (SupportMapFragment) getSupportFragmentManager()
                .findFragmentById(R.id.map);
        mapFragment.getMapAsync(this);
    }

    @Override
    public void onMapReady(GoogleMap googleMap) {
        mMap = googleMap;

        mMap.getUiSettings().setCompassEnabled(true);
        mMap.getUiSettings().setZoomControlsEnabled(true);
        mMap.getUiSettings().setZoomGesturesEnabled(true);
        mMap.setMapType(GoogleMap.MAP_TYPE_HYBRID);

        // Add a marker in Sydney and move the camera
       /* LatLng sydney = new LatLng(-34, 151);
        mMap.addMarker(new MarkerOptions().position(sydney).title("Marker in Sydney"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(sydney));*/

        Latlng mylocation=new Latlng(latitude: 28.47459562593793, longitude: 77.50271062502297);
        mMap.addMarker(new MarkerOptions().position(mylocation).title("My Location"));
        mMap.moveCamera(CameraUpdateFactory.newLatLng(mylocation));

        drawCircle(new Latlng(latitude:28.47459562593793, longitude:77.50271062502297));

    }
    private void drawCircle(Latlng latlng)
    {
        CircleOptions myoptions=new CircleOptions();
        myoptions.center(latlng);
        myoptions.radius(120);
        myoptions.strokeColor(Color.BLUE);
        myoptions.strokeWidth(2);
        myoptions.fillColor(Color.RED);
        mMap.addCircle(myoptions);
    }
}