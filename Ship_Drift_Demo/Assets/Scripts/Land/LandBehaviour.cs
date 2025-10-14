using UnityEngine;
using UnityEngine.InputSystem;

public class LandBehaviour : MonoBehaviour
{

    private Camera camera_;

    public void OnPointerClick(InputAction.CallbackContext context) {
        if(!context.started) return;
        var rayHit = Physics2D.GetRayIntersection(camera_.ScreenPointToRay(Mouse.current.position.ReadValue()));
        if(!rayHit.collider) return;
        
        Debug.Log(rayHit.collider.gameObject.name);
        PlayerContext.playerBehaviour_.Pivot = rayHit.collider.transform;
    }

    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Awake()
    {
        camera_ = Camera.main;
    }

}
