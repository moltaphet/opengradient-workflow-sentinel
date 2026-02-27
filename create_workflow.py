import os
import opengradient as og

# --- NETWORK CONFIGURATION ---
os.environ["OPENGRADIENT_ENV"] = "alpha"
PRIVATE_KEY = "pv key"

def deploy_workflow_instance():
    """
    Deploys an AI workflow using the direct workflow module.
    """
    try:
        # Initializing the SDK Client
        client = og.Client(private_key=PRIVATE_KEY)
        
        print("\n" + "="*60)
        print("🚀 INITIATING ON-CHAIN DEPLOYMENT")
        print("="*60)
        
        # FIX: Accessing deploy through the client's direct workflow interface
        # In this version, we use the client.deploy or client.workflow.deploy path
        workflow_address = client.deploy(
            model_cid="QmRhcpDXFYCKSinTmJYrAVM4Bbvck59Zb2onj3MHv9Kw5N"
        )
        
        print(f"\n[SUCCESS] WORKFLOW DEPLOYED SUCCESSFULLY!")
        print(f"[ADDRESS] {workflow_address}")
        print("-" * 60)
        print("\nACTION REQUIRED:")
        print(f"Copy the Address above and update it in your monitor.py script.")
        print("="*60 + "\n")

    except Exception as e:
        # If the direct method fails, we try the alternative internal path
        try:
            workflow_address = client.workflow.deploy(
                model_cid="QmRhcpDXFYCKSinTmJYrAVM4Bbvck59Zb2onj3MHv9Kw5N"
            )
            print(f"\n[SUCCESS] WORKFLOW DEPLOYED (via secondary path)!")
            print(f"[ADDRESS] {workflow_address}")
        except:
            print(f"\n[DEPLOYMENT ERROR]: {str(e)}")
            print("[HINT]: The Alpha SDK may have renamed the 'deploy' method.")

if __name__ == "__main__":
    deploy_workflow_instance()
