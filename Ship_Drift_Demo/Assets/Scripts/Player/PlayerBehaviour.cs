using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.Rendering;

namespace ShipDrift.Behaviour.Player {
    public class PlayerBehaviour : MonoBehaviour {

        [SerializeField]
        private float speed_;

        [SerializeField]
        private float decelSpeed_;

        [SerializeField]
        private float cannonPower_;

        [SerializeField]
        private float cannonCoolDownAmount_;

        private float cannonCoolDown_ = 0;

        [SerializeField]
        private Vector3 velocity = Vector3.zero;

        [SerializeField]
        private Transform pivot;

        public void ShootLeft(InputAction.CallbackContext value) {
            if(value.performed) {
                Shoot(-1);
            }
        }
        public void ShootRight(InputAction.CallbackContext value) {
            if(value.performed) {
                Shoot(1);
            }
        }

        private void Shoot(int direction) {
            if(cannonCoolDown_ <= 0) {
                Debug.Log((direction>0) ? "Right" : "Left");
                cannonCoolDown_ = cannonCoolDownAmount_;
                velocity += -direction * cannonPower_ * new Vector3(1, 0, 0);
            }
        }

        // Start is called once before the first execution of Update after the MonoBehaviour is created
        void Start() {

        }

        // Update is called once per frame
        void Update() {
            if(cannonCoolDown_ > 0) {
                cannonCoolDown_ -= Time.deltaTime;
            }


            transform.up = pivot.position - transform.position;

            Vector3 influencedVelocity = (velocity.y * transform.up + velocity.x * transform.right);

            transform.position += influencedVelocity * Time.deltaTime;
            velocity -= velocity.normalized*decelSpeed_*Time.deltaTime;
            

        }
    }
}